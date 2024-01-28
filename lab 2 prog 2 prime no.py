#2. Write a program to check whether given number is prime or not

print('Check prime no. or not')
a=int(input('enter the number:'))

if a == 1:
    print(a,' is not a prime no.')
else:
    for i in range(2,a):
        if a%i == 0:
            print(a,' is a not a prime no')
            break
    else:
        print(a,' is a prime no.')

