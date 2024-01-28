#5.	Write Python Program to reverse a number and also find the Sum of digits in the reversed number. Prompt the user for input.

a = input('enter the number : ')
b = int(a[::-1])
list=[]
for i in a:
    list.append(int(i))
c=0
for j in list:
    c+=j
print('reversed no is : ',b ,'\n', 'sum of the digits : ',c)


