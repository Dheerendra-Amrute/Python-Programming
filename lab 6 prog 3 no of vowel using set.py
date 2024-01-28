#3. WAP to count no of vowels using set in a given string.
str = input('Enter the string : ')
set = {"a","e","i","o","u","A","E","I","O","U"}
vowels=0
for i in str:
	if i in set:
		vowels+=1
print("No. of vowels = ",vowels)
		
		