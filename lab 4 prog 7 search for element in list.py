#7. Write Python program to perform a linear search for a given Key number in the list and report Success or Failure.

l= [1,2,5,10,20,30]
a=int(input('enter the key : '))
if a in l:
	print('success...')
else:
	print('failure...')