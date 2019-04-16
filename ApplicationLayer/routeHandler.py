from flask import jsonify
from InfrastructureLayer.routeDAO import RouteDao
from DomainLayer.route import Route


class RouteHandler:
    # Schema: 
    # Routes: route_id, route_name
    # Stops: stop_id, stop_name, latitude, longitude
    dao = RouteDao()

    def build_route_dict(self, row):
        result = {}
        result['route_id'] = row[0]
        result['route_name'] = row[1]

        return result

    def build_stop_dict(self, row):
        result = {}
        result['stop_id'] = row[0]
        result['stop_name'] = row[1]
        result['latitude'] = row[2]
        result['longitude'] = row[3]

        return result
    '''
    def build_route_stops_dict(self, row):
        result = {}
        result['route_id'] = row[0] 
        result['route_name'] = row[1] 
        result['stop_id'] = row[2] 
        result['stop_name'] = row[3] 
        result['latitude'] = row[4] 
        result['longitude'] = row[5] 

        return result
    '''
    # Gets
    def getAllRoutes(self):
        results_list = self.dao.getAllRoutes()
        routes_list = []

        for row in results_list:
            result = self.build_route_dict(row)
            routes_list.append(result)

        return jsonify(Routes=routes_list)

    def getRouteById(self, route_id):
        row = self.dao.getRouteById(route_id)

        if not row:
            return jsonify(Error="Route Not Found"), 404
        else:
            route = Route(row)
            result = route.routeInfo()
            return jsonify(Route=result)
            
    def getRouteByName(self, route_name):
        row = self.dao.getRouteByName(route_name)

        if not row:
            return jsonify(Error="Route Not Found"), 404
        else:
            route = Route(row)
            result = route.routeInfo()
            return jsonify(Route=result)

    def getRouteStops(self, route_id):
        route_data = self.dao.getRouteById(route_id)

        if not route_data: 
            return jsonify(Error="Route Not Found"), 404
        else:
            route = Route(route_data)

        results_list = self.dao.getRouteStops(route_id)
        stops_list = []

        if not results_list:
            return jsonify(Error="Route Not Found"), 404
        else:
            for row in results_list:
                route.addStop(row)

            stops_list = route.allStops()
            return jsonify(StopsInRoute=stops_list)

    def getStopById(self, stop_id):
        row = self.dao.getStopById(stop_id)

        if not row:
            return jsonify(Error="Stop Not Found"), 404
        else:
            stop = self. build_stop_dict(row)
            return jsonify(Stop=stop)

'''
    # CRUDS
    def insertUser(self):
        self.dao = UserDao()
        user = self.dao.insertUser()
        result = self.build_user_dict(user)
        return jsonify(User=result), 201

    def updateUser(self, uid, form):
        self.dao = UserDao()
        user = self.dao.update(uid)
        if not user:
            return jsonify(Error="USER NOT FOUND"), 404

        result = self.build_user_dict(user)
        return jsonify(User=result), 200

    def deleteUser(self, uid):
        return jsonify(DeleteStatus="OK"), 200

    def getCredentials(self):
        self.dao = UserDao()
        result = self.dao.getCredentials('', '')
        return jsonify(User=self.build_credential_dict(result))
    '''

