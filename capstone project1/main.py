from parking import ParkingManager
from tabulate import tabulate
"""Parking Manager application Script

"""


parking = ParkingManager(100)
#an instance of the class ParkingManager is created.

print("-"*120)
print(" -"*10,"Welcome!!! You can park the vehicles in the basement/terrace after filling in the following details","- "*10)

#application Loop
while True:

	print("\n\n")	
	print("proceed to perform the following processes\n\n")

    #print the options in the table
	print(tabulate([(1,"Checkin"),
		(2,"Checkout"),
		(3,"Parking Details"),
		(4,"Slots Available"),
		(5, "Exit")], tablefmt="fancy_grid"))
    
    # Taking the user's choice from options as (int)
	choice= input("Enter your option:")


	if choice=="1":
		"""
		If user choice is 1 (int) - checkin vehicle
		"""

        # Get Details required for checkin.
		number_plate=input("Enter the number plate value: ")
		color=input("Enter the colour of the vehicle: ")
		model=input("Enter the model of the vehicle: ")
		parking.checkin(number_plate, color, model)
	


	elif choice=="2":
		"""
		If user choice is 2 (int) - checkout vehicle
		"""
        #Get Details required during checkout
		number_plate=input("Enter the number plate value: ")
		parking.checkout(number_plate)
		

	elif choice=="3":
		"""
		If user choice is 3 (int) - for viewing the parking details.
		"""
		parking.show_details_for_admin()
		
	elif choice=="4":
		"""
		If user choice is 4 (int) - to check the slots available in the parking alltogether.
		"""
		print(f"The number of slots available in the parking are {parking.parking_slots_available}")	

	else:
		break