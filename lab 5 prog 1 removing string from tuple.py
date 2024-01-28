#1.Given a tuples containing both int and string remove all the string from tuples.

t1=('hi' ,20,40, 'hello')
L=list(t1)
L2=[]
for i in L:
	if str(i).isalpha():
		pass
	else:
		L2.append(i)
t2=tuple(L2)
print('required tuple =', t2)