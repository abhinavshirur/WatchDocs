import pickle

concept_terms=list()
concept_topics=list()
concept_categories=list()

total_concepts=list()
total_topics=list()
total_categories=list()

for i in range(4):
	str1="conceptterms"+str(i+1)+".pkl"
	str2="concepttopics"+str(i+1)+".pkl"
	str3="conceptcategories"+str(i+1)+".pkl"
	
	with open(str1,'rb') as fp:
		concept_terms=pickle.load(fp)
	with open(str2,'rb') as fp:
		concept_topics=pickle.load(fp)
	with open(str3,'rb') as fp:
		concept_categories=pickle.load(fp)
	for terms in concept_terms:
		terms=terms.split()
		for term in terms:
			total_concepts.append(term)
	for topics in concept_topics:
		for topic in topics:
			total_topics.append(topic)
	for categories in concept_categories:
		for category in categories:
			total_categories.append(category)
	

#print(len(total_concepts))
#print(len(total_topics))
#print(len(total_categories))
with open("totalconceptterms.pkl",'wb') as fp:
	pickle.dump(total_concepts,fp)
with open("totalconcepttopics.pkl",'wb') as fp:
	pickle.dump(total_topics,fp)
with open("totalconceptcategories.pkl",'wb') as fp:
	pickle.dump(total_categories,fp)