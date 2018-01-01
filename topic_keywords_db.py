# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os
import sys
import pickle


client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['topics']
collection3 = db['topic_keywords']

reload(sys)
sys.setdefaultencoding('utf8')

concept_terms=list()
concept_topics=list()
concept_categories=list()

with open("totalconceptterms.pkl",'rb') as fp:
	concept_terms=pickle.load(fp)
with open("totalconcepttopics.pkl",'rb') as fp:
	concept_topics=pickle.load(fp)

topic_keywords=dict()
for document in collection.find():
	dbtopic=document['topic']
	index=0
	keyword_list=list()
	for topic in concept_topics:
		if(dbtopic in topic):
			index=concept_topics.index(topic)
			tmpterms_list=concept_terms[index]
			tmpterms_list=tmpterms_list.split()
			for term in tmpterms_list:
				keyword_list.append(term)
	topic_keywords[dbtopic]=keyword_list

for topic in topic_keywords:
	#print(topic,topic_keywords[topic])
	post = {"topic":topic,"keywords":topic_keywords[topic]}
	post_id = collection3.insert_one(post).inserted_id