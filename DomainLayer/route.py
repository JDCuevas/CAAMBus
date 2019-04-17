from InfrastructureLayer.routeDAO import RouteDao

def routeRepository(data):
	if isinstance(data, list):
		result = []
		for row in data:
			route = Route(row)
			result.append(route.routeInfo())
	else:
		print(data)
		route = Route(data)
		result = route.routeInfo()

	return result

def routeFactory(route_name):
	dao = RouteDao()

	route_id = dao.insert(route_name)
	data = dao.getRouteById(route_id)
	route = Route(data)

	return route

class Route:
	def __init__(self, data=None):
		self.route = {}
		self.stops = []

		if data:
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