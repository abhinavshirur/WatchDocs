# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection1 = db['categories']
collection2 = db['keyword_sources']
collection3 = db['category_keywords']

show_categories=list()
for document in collection1.find():
	show_categories.append(document['category'])

for category in show_categories:
	print(category)
print("These categories are available for querying")

query=raw_input("Enter the category:")
print(query)

keywords_from_query=list()
for document in collection3.find({'category':query}):
	keywords_from_query=list(document['keywords'])
	
documents_from_keywords=set()
for keyword in keywords_from_query:
	for document in collection2.find({'keyword':keyword}):
		sources=document['sources']
		for source in sources:
			documents_from_keywords.add(source)
print("---Keywords belonging to the category---")
for keyword in keywords_from_query:
	print(keyword)
	
print("---Documents belonging to the category---")
for document in documents_from_keywords:
	print(document)