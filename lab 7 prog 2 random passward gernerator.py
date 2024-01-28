#2. Write a password generator function in python which should generate random passwords every time the user ask for a new password. Strong password should be a mix of lower case, uppercase, number and symbol.

def random_password():
    import random
    l='abcdefghijklmnopqrstuvwxyz'
    u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s='@#₹_&£€$'
    a=str(random.randint(1000,9999))
    b=''
    for i in range(4):
    	b+= l[random.randint(0,25)]
    d= u[random.randint(0,25)]
    e= s[random.randint(0,7)]
    p=(d + b + e + a)
    return p

print('password = ',random_password())
