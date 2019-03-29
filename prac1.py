#Read Input String 
i = input("Please insert characters: ")
#Index through the entire string
for index in range(len(i)):
    #Check if odd 
    if(index % 2 == 0):
        #print odd characters
        print(i[index])
