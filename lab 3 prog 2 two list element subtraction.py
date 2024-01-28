#2.	Substract two list elements and output new list if the element in the first list are greater.
list1 = [5,6,7,8,10]
list2 = [1,20,9,11,12]
list = []
for i in list1:
    for j in list2:
        if i>j:
            list.append(i-j)
        else:
            continue
print(list)
