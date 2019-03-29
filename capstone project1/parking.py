
"""Parking Manager Module

"""
from datetime import datetime
from tabulate import tabulate


class ParkingManager:
	""" General parking class for a Parking Manager
	"""
	
	def __init__(self, parking_slots_available):
		""" Constructor function for Parking class 
		    executed by the interpreter to create an instance of this class
            
            Attributes:
             self.parking_slots_available -- gives the number of parking slots which are available in the Parking(int).

		 """
		self.parking_details = {}
		#represents a dictionary which which store all the details of the vehicles which are parked.
		self.parking_slots_available=parking_slots_available



	def checkin(self,number_plate,color,model):
		"""checks in the vehicles which arrive on taking the following details
		   params:
		   number_plate--the registered number of the vehile.
		   color--the color of the vehicle.
		   model--the model of the vehicle.
		"""
		self.parking_details[number_plate]={'start_time': datetime.now(), 'color': color , 'model': model}
		self.parking_slots_available-=1
	

	 
	def checkout(self, number_plate):
		"""checks out the vehicle which has been parked by accesing the already registered number plate of the vehicle
		   params:
		   number_plate--the registered number plate is retrieved for checkout.
	    """
		self.parking_details[number_plate]["end_time"] = datetime.now()
		self.parking_slots_available+=1
		self.price_calculation(number_plate)
		del self.parking_details[number_plate]
		


	def show_details_for_admin(self):
		""" returns the parking details 
		"""
		table = [[key, vehicle['model'], vehicle['color'], vehicle['start_time']] for key, vehicle in self.parking_details.items() ]
		headers = ["Number Plate", "Model", "Color", "Checkin Time"]
		print(tabulate(table, headers, tablefmt="pipe"))
 
	def price_calculation(self, number_plate):
		"""calcutes the price charged on the vehicle which is parked on evaluating the difference between the checkin time and the checkout time
		   params:
		   number_plate--the registered number plate is retrieved for calculating the price to be paid. """
		rate_slab={}
		rate_slab[2]=10
		rate_slab[4]=20
		rate_slab[6]=30
		rate_slab[8]=50
		#rates for every two hours is as stated above.

		vehicle = self.parking_details[number_plate]
		
		total_time = vehicle["end_time"] - vehicle["start_time"]
		total_time_in_hours = total_time.seconds / (60*60)

		if total_time_in_hours <= 2:
			print(f"Rate is {rate_slab[2]}")
		elif total_time_in_hours > 2 and total_time_in_hours <= 4:
			print(f"Rate is {rate_slab[4]}")
		elif total_time_in_hours > 4 and total_time_in_hours <= 6:
			print(f"Rate is {rate_slab[6]}")
		elif total_time_in_hours > 6 and total_time_in_hours <= 8:
			print(f"Rate is {rate_slab[8]}")
		else:
			print("Cannot park a vehicle for more than 8 hours!!vehicle seized. 😜")

class BasementPakingManager(ParkingManager):
	"""Speific parking class for a parking manager
	"""
	def __init__(self,parking_slots_available):
		self.parking_details={}
		self.parking_slots_available=parking_slots_available	

 					 			
class TerraceParkingManager(ParkingManager):
	"""Speific parking class for a parking manager
	"""
	def __init__(self,parking_slots_available):
		self.parking_details={}
		self.parking_slots_available=parking_slots_available
		pass
	def price_calculation(self,number_plate):
		pass	
					
		

 

if __name__ == "__main__":
	"""Test Cases
	"""
	vehicle1=ParkingManager(100)
	vehicle1.show_details_for_admin()
	vehicle1.checkin('ka01','blue','swift')
	vehicle1.show_details_for_admin()
	vehicle1.checkout('ka01')
	vehicle1.show_details_for_admin()
	vehicle1.price_calculation('ka01')
	vehicle1.show_details_for_admin()
	vehicle2=BasementPakingManager(60)
	vehicle2.checkin('ka02','black','innova')
	vehicle2.show_details_for_admin()
	vehicle2.checkout('ka02')
	vehicle2.show_details_for_admin()
	vehicle2.price_calculation('ka02')
	vehicle3=TerraceParkingManager(40)
	vehicle3.checkin('ka03','green','alto')
	vehicle3.show_details_for_admin()
