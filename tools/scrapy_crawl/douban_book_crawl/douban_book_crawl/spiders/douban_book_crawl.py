from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath
 
def myjoin(base, url):
    url1 = urljoin(base, url)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme, arr.netloc, path, arr.params, arr.query, arr.fragment))

class DoubanBookCrawl(Spider):
	name = "douban_book_crawl"
	allowed_domains = ["book.douban.com"]

	start_urls = [
		"https://book.douban.com/tag/",
	]

	def start_requests(self):
		yield Request("https://book.douban.com/tag/", headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

	def parse_list(self, response):
		print '\nparsing book_of_tag list: ', response.url

		base_url = "https://api.douban.com/v2/book"

		sel = Selector(response)

		book_urls = sel.xpath("//ul[@class='subject-list']/li[@class='subject-item']/div[@class='info']/h2/a/@href").extract()
		print '\n-------------------------------- Start Parsing Book In The Book_Url --------------------------------'

		for book_url in book_urls:
			#print 'book_url', book_url
			# select the book id
			book_id_temp = book_url[31:]
			book_id = book_id_temp[:-1]
			req_book_url = base_url + book_id
			print 'req_book_url', req_book_url

		print '-------------------------------- Finish Parsing Book In The Book_Url --------------------------------\n'


	def parse_tag(self, response):
		print '\nparse_tag url is ', response.url

		for i in range(0, 99):
			req_url = response.url + "?start=" + str(20 * i) + "&type=T"
			print 'req_url in this page is ', req_url
			yield Request(req_url, headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}, callback=self.parse_list)


	def parse(self, response):
		base_url = "https://book.douban.com"
		print '\n################################ Start Parsing Tags In The Start_Url ################################'
		print 'parsing', response.url

		sel = Selector(response)

		# tag_urls = sel.xpath("//table[@class='tagCol']/tbody/tr/td/a/@href").extract()
		# print '################################ Finish Parsing Tags In The Start_Url ################################\n'

		# print '\n********************************* Start Parsing Book List In One Tag Page *********************************'
		# for tag_url in tag_urls:
		# 	print 'tag_url: ', myjoin(base_url, tag_url)
		# 	yield Request(myjoin(base_url, tag_url), headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}, callback=self.parse_tag)

		# print '********************************* Finish Parsing Book List In One Tag Page *********************************\n'
		
		tag_url = sel.xpath("//table[@class='tagCol']/tbody/tr/td/a/@href").extract()[0]
		print '################################ Finish Parsing Tags In The Start_Url ################################\n'

		print '\n********************************* Start Parsing Book List In One Tag Page *********************************'
		yield Request(base_url+tag_url, headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}, callback=self.parse_tag)

		print '********************************* Finish Parsing Book List In One Tag Page *********************************\n'


	