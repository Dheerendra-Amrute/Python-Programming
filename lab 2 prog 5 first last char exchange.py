#P-5.Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
a = str(input('Enter the string : '))

print(a[-1]+ a[1:-1]+ a[0])