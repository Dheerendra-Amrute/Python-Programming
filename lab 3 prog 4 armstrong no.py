#4.	Write a Python program to check if a 3 digit number is Armstrong number or not.

a=(input('enter the no : '))
list=[]
for i in a:
    list.append(int(i))
b=0
for j in list:
    b = b + (j**len(a))

if int(a) == b:
    print(a, ' is an armstrong number')
else:
    print(a, ' is not an armstrong number')