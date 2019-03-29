from events import add_participant,see_participant
while True:
	choice=input("enter your choice:\n\
		1.Add participant\n\
		2.see participant")
	if choice=='1':
		add_participant()
	elif choice=='2':
		see_participant()
	else:
		break		
