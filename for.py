n=int(input("enter no of elements"))
count=0
list1=[]
list2=[]
for i in range(0,n):
    a=int(input("enter element"))
    list1.append(a)
print(list1)
for j in range(0,n):
    b=int(input("enter element"))
    list2.append(b)
print(list2)
for k in range(0,n):
    if list1[k] in list1 and  list1[k] in list2:
        print(list1[k])
        count+=1
        b=list1[k]
        list1.remove(b)
        list2.remove(b)
print(count)      
print(list1)
print(list2)
