from InfrastructureLayer.itineraryDAO import ItineraryDao

def itineraryRepository(data):
	if isinstance(data, list):
		result = []
		for row in data:
			itinerary = Itinerary(row)
			result.append(itinerary)
	else:
		print(data)
		itinerary = Itinerary(data)
		result = itinerary

	return result

def getInfo(itinerary):
	return itineraryInfo.info()

def itineraryFactory(date, start_time, end_time, driver_id, trolley_id, route_id):
	dao = ItineraryDao()

	itinerary_id = dao.insert(date, start_time, end_time, driver_id, trolley_id, route_id)
	data = dao.getItineraryById(itinerary_id)
	itinerary = Itinerary(data)

	return itinerary

class Itinerary:
	def __init__(self, data=None):
		self.itinerary = {}

		if len(data) <= 7:
			self.itinerary['itinerary_id'] = data[0]
			self.itinerary['date'] = data[1].__str__()
			self.itinerary['start_time'] = data[2].__str__()
			self.itinerary['end_time'] = data[3].__str__()
			self.itinerary['driver_id'] = data[4]
			self.itinerary['trolley_id'] = data[5]
			self.itinerary['route_id'] = data[6]
		else:
			self.fullItineraryInfo(data)

	def info(self):
		return self.itinerary

	def fullItineraryInfo(self, data):
			self.itinerary['itinerary_id'] = data[0]
			self.itinerary['date'] = data[1].__str__()
			self.itinerary['start_time'] = data[2].__str__()
			self.itinerary['end_time'] = data[3].__str__()
			self.itinerary['driver_id'] = data[4]
			self.itinerary['first_name'] = data[5]
			self.itinerary['last_name'] = data[6]
			self.itinerary['license'] = data[7]
			self.itinerary['phone'] = data[8]
			self.itinerary['trolley_id'] = data[9]
			self.itinerary['plate'] = data[10]
			self.itinerary['capacity'] = data[11]
			self.itinerary['mileage'] = data[12]
			self.itinerary['route_id'] = data[13]
			self.itinerary['route_name'] = data[14]