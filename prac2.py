list1=[]
list2=[]
for i in range(3):
	a=int(input("enter the usn:"))
	b=input("enter the name:")
	list1.append(a)
	list2.append(b)	
dict1={}
for j in list1:
	dict1[list1[j]]=list2[j]
print(dict1)
