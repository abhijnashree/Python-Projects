events_dict={'1':'CS 1.G','2':'Google It','3':'Treasure It'}
participant_details={}
def add_participant():
	name=input("Enter the name of participant:")
	event=input("Enter the serial number of an event from the following list:\n\
		1.CS\n\
		2.Google it\n\
		3.Treasure Hunt\n")

	participant_details[name]=events_dict[event]
	return participant_details


def see_participant():
	for key,value in participant_details.items():
		print(key,value,sep='-')

if __name__ == '__main__':
	add_participant()
	print(participant_details)
	see_participant()	