#1. Write a python program to read file contain and store that information in another file.

c=open('myfile.txt','r')
a= c.read()
print('file content :\n',a)
c.close()

f = open('newfile.txt','w')
f.write(a)
print('data stored in new file successfully...')
f.close()

d=open('newfile.txt','r')
print('newfile content :\n',d.read())
d.close()

