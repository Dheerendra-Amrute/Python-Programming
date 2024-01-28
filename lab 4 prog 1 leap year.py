# 1. Write Pythonic code to check if a given year is a leap year or not.
a= int(input("enter the year: "))
if (a%4 == 0 and a%100 != 0)or a%400 == 0:
	print(a," is leap Year" )
else:
	print(a,"is not a leap year")