#2. Write a program to count the unique tuples in a list and remove the duplicate tuples.

L= [(1,2,3),(3,4,5),(1,2,3)]
L2 = []
for i in L:
	
		if (L.count(i)>1):
			pass
		else:
			L2.append(i)
t2=tuple(L2)
			
		
print('No. of uniqe tuple =',len(L2) ,' and that tuple is = ', t2)
