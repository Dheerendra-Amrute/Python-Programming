#3. Write a program to calculate min and max values from a list of tuples
L= [(1,2,3),(3,4,5),(6,7,8)]
l3=[]
for i in L:
	l3.extend(i)
print('maximum value=', max(l3) ,'minimum value',min(l3))

