class Trolley:
	def __init__(self, data):
		self.trolley = {}
		self.trolley['trolley_id'] = data[0]
		self.trolley['plate'] = data[1]
		self.trolley['capacity'] = data[2]
		self.trolley['mileage'] = data[3]

	def trolleyInfo(self):
		return self.trolley