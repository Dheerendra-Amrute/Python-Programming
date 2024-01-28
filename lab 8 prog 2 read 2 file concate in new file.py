#2.	Write a python program to read two files and concate it output and write it in third file.

c=open('11.txt','r')
a= c.readline()
b=c.readline()
c.close()

d=open('12.txt','r')
x=d.readline()
y=d.readline()
d.close()

z=open('output.txt','w+')
z.writelines([a.strip()+x,b+y])
z.close()

f=open('output.txt','r')
print(f.read())
f.close()