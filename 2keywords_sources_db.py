# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os
import sys

client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['keyword_sources']
collection2 = db['keywords']

reload(sys)
sys.setdefaultencoding('utf8')

dir_path='D:\Study\Final Year Sem 1\Project\Programs\WatchDocs\Test documents'
for document in collection2.find():
	keyword=document['keyword']
	obj_id=document['_id']
	keyword_sources=list()
	for filename in os.listdir(dir_path):
		file = open(dir_path+'\\'+filename,"r") 
		fileContents = file.read()
		stringOfText = fileContents
		stringOfText=stringOfText.lower()
		stringOfText=stringOfText.decode('utf-8')
		if keyword in stringOfText:
			keyword_sources.append(file.name)
		#print(keyword['keyword'])
		#i=i+1
		#if(i==11):
			#break
		#print(keyword+' and its Source is:'+str(keyword_sources)+'\n')
	post = {"_id":obj_id,"keyword":keyword,"sources":keyword_sources}
	post_id = collection.insert_one(post).inserted_id