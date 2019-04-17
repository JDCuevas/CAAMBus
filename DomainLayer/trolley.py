from InfrastructureLayer.trolleyDAO import TrolleyDao

def trolleyRepository(data):
	if isinstance(data, list):
		result = []
		for row in data:
			trolley = Trolley(row)
			result.append(trolley.trolleyInfo())
	else:
		print(data)
		trolley = Trolley(data)
		result = trolley.trolleyInfo()

	return result

def trolleyFactory(plate, capacity, mileage):
	dao = TrolleyDao()

	trolley_id = dao.insert(plate, capacity, mileage)
	data = dao.getTrolleyById(trolley_id)
	trolley = Trolley(data)

	return trolley

class Trolley:
	def __init__(self, data=None):
		self.trolley = {}

		if data:
			self.trolley['trolley_id'] = data[0]
			self.trolley['plate'] = data[1]
			self.trolley['capacity'] = data[2]
			self.trolley['mileage'] = data[3]

	def trolleyInfo(self):
		return self.trolley