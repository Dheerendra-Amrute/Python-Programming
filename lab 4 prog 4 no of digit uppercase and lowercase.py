#4. Write a program that accepts a sentence and calculate the number of digits, uppercase and lowercase letters.

a= input('Enter the sentence : ')
digits=0
uppercase=0
lowercase=0
for i in a:
	if i.isnumeric():
		digits+=1
	elif i.isupper():
		uppercase+=1
	elif i.islower():
		lowercase+=1

print('Number of digits : ',digits ,'\nUppercase : ',uppercase,'\nLowecase : ',lowercase)
		
		