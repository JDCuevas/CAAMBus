from InfrastructureLayer.driverDAO import DriverDao

def driverRepository(data):
	if isinstance(data, list):
		result = []
		for row in data:
			driver = Driver(row)
			result.append(driver.driverInfo())
	else:
		print(data)
		driver = Driver(data)
		result = driver.driverInfo()

	return result

def driverFactory(frist_name, last_name, license, phone):
	dao = DriverDao()

	driver_id = dao.insert(frist_name, last_name, license, phone)
	data = dao.getDriverById(driver_id)
	driver = Driver(data)

	return driver

class Driver:
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