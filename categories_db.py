import pickle
import sys
from pymongo import MongoClient
import sys

reload(sys)
sys.setdefaultencoding('utf8')

client = MongoClient('localhost', 27017)
db = client['watchdocs']
collection = db['categories']

categories=list()
allcategories=set()
with open("totalconceptcategories.pkl",'rb') as fp:
	categories=pickle.load(fp)

for category in categories:
		for category_one in category:
			allcategories.add(category_one)
allcategories=sorted(allcategories)
print(allcategories)
print(len(allcategories))


for category in allcategories:
	post = {"category":category}
	post_id = collection.insert_one(post).inserted_id