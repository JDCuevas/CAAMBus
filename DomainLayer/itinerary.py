class Itinerary:
	def __init__(self, itinerary_id=None, date=None, start_time=None, end_time=None, driver_id=None, trolley_id=None, route_id=None):
		self.itinerary_id = itinerary_id
		self.date = date
		self.start_time = start_time
		self.end_time = end_time
		self.driver_id = driver_id
		self.trolley_id = trolley_id
		self.route_id = route_id