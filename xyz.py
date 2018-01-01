import pickle
import sys

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


'''print("---Document terms---")
for term in concept_terms:
	print(term.decode('utf-8'))
print("---Document topics---")
for topic in concept_topics:
	print(topic)'''
print("---Document categories---")
for category in concept_categories:
	print(category)
