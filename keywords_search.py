# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection1 = db['keywords']
collection2 = db['keyword_sources']
collection3 = db['keyword_topics']
collection4 = db['keyword_categories']

keyword=raw_input("Enter a keyword:")
for document in collection3.find({'keyword':keyword}):
	topics=document['topics']
	'''print("---Term topics---")
	for topic in topics:
		topic.encode('utf-8')
		print(topic)'''
for document in collection2.find({'keyword':keyword}):
	sources=document['sources']
	print("---Term sources---")
	for source in sources:
		print(source)
for document in collection4.find({'keyword':keyword}):
	categories=document['categories']
	print("---Term categories---")
	for category in categories:
		print(category)