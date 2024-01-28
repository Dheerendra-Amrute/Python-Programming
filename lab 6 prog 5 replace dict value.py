#5. Write a python program to create computer accessory dictionary and  replace dictionary value if price is less than 500.

mouse= {'company':'intex','model':'INTEX2022','price':250}
keyboard={'company':'zebronics','model':'ZEB2022','price':350}
monitor={'company':'dell','model':'dellOLED2023','price':5000}
speaker = {'company':'boat','model':'INTEX2022','price':2550}
comp_acc = {'mouse':mouse, 'keyboard':keyboard,'monitor':monitor,'speaker':speaker}

print('Before Replacement :')
print(comp_acc,'\n')

for i in comp_acc:
	if comp_acc[i]['price']<500:
		print('price of ',i,' is less than 500')
		a=int(input('enter the new price :'))
		comp_acc[i]['price'] = a
		print('price changed successfully...\n')

print('After Replacement :')
print(comp_acc)

