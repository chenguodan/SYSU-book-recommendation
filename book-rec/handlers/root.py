#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import math
from BaseHandler import *

from modules.db.helper import book
from modules.db.helper import bookLabel
from modules.db.helper import user



quantityOfPopularBook = 10
# 热门标签个数
sizeOfGetLabelsMethod = 10
# 某类标签的书本数
sizeOfGetBooksByLabelMethod = 10
# 标签页中的标签数
LabelCountPerPage = 10
# 查询结果每页的书本数
searchBookCountPerPage = 10
# 所有查询结果数量
allResultCount = 1000000

def formatToBookList(books):
	bookList = []
	for book in books:
		temp = [book.uid, book.name, book.imgUrl]
		bookList.append(temp)
		temp = []
	return bookList


def formatToPopularLabelList(bookLabels):
	labelList = []
	for label in bookLabels:
		labelList.append(label.name)
	return labelList

def calcPage(total, perPage):
	return int(math.ceil(total / perPage))

def formatToAllLabelList(labels):
	labelList = []
	for label in labels:
		labelList.append(label.name)
	return labelList

