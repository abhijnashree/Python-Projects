dictionary1={}
for i in range(3):
	key=input("enter usn: ")
	val=input("enter name: ")
	if key not in dictionary1.keys():
		dictionary1[key]=val
print(dictionary1)

