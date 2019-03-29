string="Winter Is Coming!"
str_2=''
for letter in string:
	if letter.isupper():
		str_2=str_2+letter.lower()
	elif letter.islower():
			str_2=str_2+letter.upper()
	else:
		str_2=str_2+letter
print(str_2)		

