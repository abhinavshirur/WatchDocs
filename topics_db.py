import pickle
import sys
from pymongo import MongoClient
import sys

reload(sys)
sys.setdefaultencoding('utf8')

client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['topics']

topics=list()
alltopics=set()
with open("totalconcepttopics.pkl",'rb') as fp:
	topics=pickle.load(fp)

for topic in topics:
		for topic_one in topic:
			alltopics.add(topic_one)
alltopics=sorted(alltopics)
print(alltopics)
print(len(alltopics))


for topic in alltopics:
	post = {"topic":topic}
	post_id = collection.insert_one(post).inserted_id