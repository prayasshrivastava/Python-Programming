adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]
for i in ad:
    if i>5:
        list1.append(i)
for i in ad:
    if i<=2:
        list2.append(i)
print("Numbers which are greater than 5:")
print(list1)
print("numbers which are less than or equals to 2:")
print(list2)
