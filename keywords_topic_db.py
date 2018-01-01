# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os
import sys
import pickle


client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['keyword_topics']
collection2 = db['keywords']
collection3 = db['keyword_topics']
collection4 = db['keyword_categories']

reload(sys)
sys.setdefaultencoding('utf8')

concept_terms=list()
concept_topics=list()
concept_categories=list()

with open("totalconceptterms.pkl",'rb') as fp:
	concept_terms=pickle.load(fp)
with open("totalconcepttopics.pkl",'rb') as fp:
	concept_topics=pickle.load(fp)
with open("totalconceptcategories.pkl",'rb') as fp:
	concept_categories=pickle.load(fp)

keyword_topics=dict()
keyword_categories=dict()
for document in collection2.find():
	keyword=document['keyword']
	index=0
	topics_list=list()
	categories_list=list()
	for term in concept_terms:
		if(keyword in term):
			index=concept_terms.index(term)
			tmptopics_list=concept_topics[index]
			tmpcategories_list=concept_categories[index]
			for topic in tmptopics_list:
				topics_list.append(topic)
			for category in tmpcategories_list:
				categories_list.append(category)
	keyword_topics[keyword]=topics_list
	keyword_categories[keyword]=categories_list

for keyword in keyword_topics:
	#print(keyword,keyword_topics[keyword])
	post = {"keyword":keyword,"topics":keyword_topics[keyword]}
	post_id = collection3.insert_one(post).inserted_id
for keyword in keyword_categories:
	#print(keyword,keyword_categories[keyword])
	post = {"keyword":keyword,"categories":keyword_categories[keyword]}
	post_id = collection4.insert_one(post).inserted_id