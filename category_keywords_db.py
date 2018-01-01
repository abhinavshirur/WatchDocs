# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os
import sys
import pickle


client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['categories']
collection3 = db['category_keywords']

reload(sys)
sys.setdefaultencoding('utf8')

concept_terms=list()
concept_topics=list()
concept_categories=list()

with open("totalconceptterms.pkl",'rb') as fp:
	concept_terms=pickle.load(fp)
with open("totalconceptcategories.pkl",'rb') as fp:
	concept_categories=pickle.load(fp)

category_keywords=dict()
for document in collection.find():
	dbcategory=document['category']
	index=0
	keyword_list=list()
	for category in concept_categories:
		if(dbcategory in category):
			index=concept_categories.index(category)
			tmpterms_list=concept_terms[index]
			tmpterms_list=tmpterms_list.split()
			for term in tmpterms_list:
				keyword_list.append(term)
	category_keywords[dbcategory]=keyword_list

for category in category_keywords:
	#print(category,category_keywords[category])
	post = {"category":category,"keywords":category_keywords[category	]}
	post_id = collection3.insert_one(post).inserted_id