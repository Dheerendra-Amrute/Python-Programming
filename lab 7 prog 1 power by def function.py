# 1. Write a function to calculate the power of number raised to other.
def Power(a,b):
	c=(a**b)
	return c

a=int(input('Enter the first no. : '))
b=int(input('Enter the second no. : '))
print('the power of no. raised to another is  : ',Power(a,b))
