import pickle
import sys
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['keywords']

terms=list()
keywords=set()
with open("totalconceptterms.pkl",'rb') as fp:
	terms=pickle.load(fp)

for term in terms:
	term=term.split()
	for words in term:
		keywords.add(words)
keywords=sorted(keywords)
#print(keywords)
#print(len(keywords))


for keyword in keywords:
	post = {"keyword":keyword}
	post_id = collection.insert_one(post).inserted_id