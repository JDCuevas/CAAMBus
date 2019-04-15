from flask import jsonify
from InfrastructureLayer.routeDAO import RouteDao


class RouteHandler:
    # Schema: 
    # Routes: route_id, route_name
    # Stops: stop_id, stop_name, latitude, longitude

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

    def build_route_stops_dict(self, row):
        result = {}
        result['route_id'] = row[0] 
        result['route_name'] = row[1] 
        result['stop_id'] = row[2] 
        result['stop_name'] = row[3] 
        result['latitude'] = row[4] 
        result['longitude'] = row[5] 

        return result
    
    # Gets
    def getAllRoutes(self):
        dao = RouteDao()
        results_list = dao.getAllRoutes()
        routes_list = []

        for row in results_list:
            result = self.build_route_dict(row)
            routes_list.append(result)

        return jsonify(Routes=routes_list)

    def getRouteById(self, route_id):
        dao = RouteDao()
        row = dao.getRouteById(route_id)

        if not row:
            return jsonify(Error="Route Not Found"), 404
        else:
            route = self. build_route_dict(row)
            return jsonify(Route=route)

    def getRouteByName(self, route_name):
        dao = RouteDao()
        row = dao.getRouteByName(route_name)

        if not row:
            return jsonify(Error="Route Not Found"), 404
        else:
            route = self. build_route_dict(row)
            return jsonify(Route=route)

    def getRouteStops(self, route_id):
        dao = RouteDao()
        results_list = dao.getRouteStops(route_id)
        stops_list = []

        if not results_list:
            return jsonify(Error="Route Not Found"), 404
        else:
            for row in results_list:
                result = self.build_route_stops_dict(row)
                stops_list.append(result)
            return jsonify(StopsInRoute=stops_list)

    def getStopById(self, stop_id):
        dao = RouteDao()
        row = dao.getStopById(stop_id)

        if not row:
            return jsonify(Error="Stop Not Found"), 404
        else:
            stop = self. build_stop_dict(row)
            return jsonify(Stop=stop)

'''
    # CRUDS
    def insertUser(self):
        dao = UserDao()
        user = dao.insertUser()
        result = self.build_user_dict(user)
        return jsonify(User=result), 201

    def updateUser(self, uid, form):
        dao = UserDao()
        user = dao.update(uid)
        if not user:
            return jsonify(Error="USER NOT FOUND"), 404

        result = self.build_user_dict(user)
        return jsonify(User=result), 200

    def deleteUser(self, uid):
        return jsonify(DeleteStatus="OK"), 200

    def getCredentials(self):
        dao = UserDao()
        result = dao.getCredentials('', '')
        return jsonify(User=self.build_credential_dict(result))
    '''

