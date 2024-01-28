def rec_factorial(a):
	b=1
	if a>0:
		b*=a*rec_factorial(a-1)
		
	else:
		result =1
		return result
	return b
while True:
	a= int(input('Enter the no = '))
	print(rec_factorial(a))
		
		