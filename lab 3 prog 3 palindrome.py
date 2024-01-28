#3.	Print all the pelindrom numbers in a list.
a = input('enter the number or string : ')
if a == a[::-1]:
        print(a,' is a palindrome')
else:
        print(a,' is not a palindrome')
