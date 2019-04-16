class Route:
	def __init__(self, data=None):
		self.route = {}
		self.stops = []

		self.route['route_id'] = data[0]
		self.route['route_name'] = data[1]

	def routeInfo(self):
		return self.route

	def allStops(self):
		return self.stops

	def addStop(self, data):
		stop = {}
		stop['stop_id'] = data[0]
		stop['stop_name'] = data[1]
		stop['latitude'] = data[2]
		stop['longitude'] = data[3]

		self.stops.append(stop) 

	def routeWithStops(self):
		result_list = []

		for stop in self.stops:
			result = {}
			result['route_id'] = self.route['route_id']
			result['route_name'] = self.route['route_name']
			result['stop_id'] = stop['stop_id']
			result['stop_name'] = stop['stop_name']
			result['latitude'] = stop['latitude']
			result['longitude'] = stop['longitude']

			result_list.append(result)

		return result_list