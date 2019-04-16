class Driver:
	'''
	def __init__(self, driver_id=None, first_name=None, last_name=None, license=None, phone=None):
		self.driver_id = driver_id
		self.first_name = first_name
		self.last_name = last_name
		self. license = license
		self.phone = phone
	'''

	def __init__(self, data=None):
		self.driver = {}

		if data:
			self.driver['driver_id'] = data[0]
			self.driver['first_name'] = data[1]
			self.driver['last_name'] = data[2]
			self.driver['license'] = data[3]
			self.driver['phone'] = data[4]

	def driverInfo(self):
		return self.driver