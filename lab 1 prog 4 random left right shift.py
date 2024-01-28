#P-4. Write a program to generate two random number and perform left
#     and right shift of generated number.

import random
a = random.randint(0,9)
print (a)
b = random.randint(0,9)
print (b)
print ('left shift=' , a<<b)
print ('right shift=' , a>>b)

