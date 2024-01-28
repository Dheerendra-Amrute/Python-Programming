#6. Write a python program to match key values in two dictionary.

dict1={'laptop': 'HP','color':'Black','price':50000,'ram':'8gb'}
dict2={'laptop': 'ACER','color':'Black','price':50000,'ram':'16gb'}
for i in dict1:
	if dict1[i] == dict2[i]:
		print(i ,':',dict1[i],"is same in both dictionary")
		