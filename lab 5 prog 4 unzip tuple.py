#4. 
t1 = ((1,2,3),(3,4,5),(6,7,8))
L = list(t1)
l3=[]
for i in t1:
	l3.extend(i)

t3= tuple(l3)
print('unziped tuple= ',t3)