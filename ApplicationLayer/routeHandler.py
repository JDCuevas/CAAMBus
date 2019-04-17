from flask import jsonify
from InfrastructureLayer.routeDAO import RouteDao
from DomainLayer.route import Route, routeRepository, routeFactory


class RouteHandler:
    # Schema: 
    # Routes: route_id, route_name
    # Stops: stop_id, stop_name, latitude, longitude
    dao = RouteDao()

    # Gets
    def getAllRoutes(self):
        results_list = self.dao.getAllRoutes()
        routes_list = []

        routes_list = routeRepository(results_list)

        return jsonify(Routes=routes_list)

    def getRouteById(self, route_id):
        result = self.dao.getRouteById(route_id)

        if not result:
            return jsonify(Error="Route Not Found"), 404
        else:
            route = routeRepository(result)
            return jsonify(Route=route)

    def getRouteByName(self, route_name):
        result = self.dao.getRouteByName(route_name)

        if not result:
            return jsonify(Error="Route Not Found"), 404
        else:
            route = routeRepository(result)
            return jsonify(Route=route)

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

