#2. Write Python program to count the total number of vowels, consonants and blanks in a String.
str = input("Enter the string : ")
vowels = 0
consonants = 0
blanks = 0
for i in str:
	if i == "a" or i=="e" or i=="i" or i== "o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
		vowels += 1
		
	elif i == ' ':
		blanks += 1
		
	else:
		consonants += 1
print("Vowels = ",vowels,"consonants = ",consonants,"Blanks = ",blanks)