# P-2 Write a python program to design calculator

'''Press the button according to operation :-
press + - For Addition
press - - For Substraction
press / - For Division
press * - For Multiplication
press ** - For Exponential
press // - For floor division
press % - For modulus
'''
a = float(input('enter the first no.-'))
c= str(input('Press the button according to operation :-')) # operation you want
b = float(input('enter the second no.-'))
if c == '+' :
    print(a+b)           #Addition
if c == '-':
    print(a-b)           #Substraction
if c == '/':
    print(a/b)           #Division
if c == '*':
    print(a*b)           #Multiplication
if c == '**':
    print(a**b)          #Exponential
if c == '//':
    print(a//b)          #floor division
if c == '%':
    print(a%b)           #For modulus

