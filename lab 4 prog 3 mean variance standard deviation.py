#3. Write Pythonic code to find Mean, Variance and Standard Deviation for a list of numbers.

L=[1,2,3,4,5,6]
a=sum(L)/len(L)
print('Mean : ', a)
b=0
for i in L:
	b+=((i-a)**2)
print('Variance : ' ,b/len(L))
print('Standard deviation : ' , (b/len(L))**(1/2))
