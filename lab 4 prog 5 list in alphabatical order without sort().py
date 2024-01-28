#5. Write Pythonic code to sort a sequence of names according to their alphabetical order without using sort() function.

l=['pineapple','apple','mango','banana','cherry','Apple']
l2 = []
for i in range(len(l)):
	l2.append(min(l))
	l.remove(min(l))
print(l2)