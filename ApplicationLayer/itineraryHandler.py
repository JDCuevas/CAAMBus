from flask import jsonify
from InfrastructureLayer.itineraryDAO import ItineraryDao

class ItineraryHandler:
    # Schema: itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id

    def build_itinerary_dict(self, row):
        result = {}
        result['itinerary_id'] = row[0]
        result['date'] = row[1].__str__()
        result['start_time'] = row[2].__str__()
        result['end_time'] = row[3].__str__()
        result['driver_id'] = row[4]
        result['trolley_id'] = row[5]
        result['route_id'] = row[6]

        return result

    def build_full_itinerary_dict(self, row):
        result = {}
        result['itinerary_id'] = row[0]
        result['driver_id'] = row[1]
        result['trolley_id'] = row[2]
        result['route_id'] = row[3]
        result['date'] = row[4].__str__()
        result['start_time'] = row[5].__str__()
        result['end_time'] = row[6].__str__()
        result['first_name'] = row[7]
        result['last_name'] = row[8]
        result['license'] = row[9]
        result['phone'] = row[10]
        result['plate'] = row[11]
        result['capacity'] = row[12]
        result['mileage'] = row[13]
        result['route_name'] = row[14]

        return result

    # Gets
    def getAllItineraries(self):
        dao = ItineraryDao()
        result_list = dao.getAllItineraries()
        itinerary_list = []

        for row in result_list:
            result = self.build_itinerary_dict(row)
            itinerary_list.append(result)

        print(itinerary_list)

        return jsonify(Itineraries=itinerary_list)


    def getItineraryById(self, itinerary_id):
        dao = ItineraryDao()
        result = dao.getItineraryById(itinerary_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = self.build_itinerary_dict(result)
            return jsonify(Itinerary=itinerary)

    def getItinerariesByDate(self, date):
        dao = ItineraryDao()
        result_list = dao.getItinerariesByDate(date)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                result = self.build_itinerary_dict(row)
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByStartTime(self, start_time):
        dao = ItineraryDao()
        result_list = dao.getItinerariesByStartTime(start_time)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                result = self.build_itinerary_dict(row)
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByEndTime(self, end_time):
        dao = ItineraryDao()
        result_list = dao.getItinerariesByEndTime(end_time)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                result = self.build_itinerary_dict(row)
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByDriverId(self, driver_id):
        dao = ItineraryDao()
        result = dao.getItinerariesByDriverId(driver_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = self.build_itinerary_dict(result)
            return jsonify(Itinerary=itinerary)

    def getItinerariesByTrolleyId(self, trolley_id):
        dao = ItineraryDao()
        result = dao.getItinerariesByTrolleyId(trolley_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = self.build_itinerary_dict(result)
            return jsonify(Itinerary=itinerary)

    def getItinerariesByRouteId(self, route_id):
        dao = ItineraryDao()
        result = dao.getItinerariesByRouteId(route_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = self.build_itinerary_dict(result)
            return jsonify(Itinerary=itinerary)

    def getFullItineraryDetails(self, itinerary_id):
        dao = ItineraryDao()
        result = dao.getFullItineraryDetails(itinerary_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = self.build_full_itinerary_dict(result)
            return jsonify(Itinerary=itinerary)

'''
    # CRUDS
    def insertUser(self):
        dao = UserDao()
        user = dao.insertUser()
        return jsonify(User=user), 201
    def updateUser(self, uid, form):
        dao = UserDao()
        user = dao.update(uid)
        if not user:
            return jsonify(Error="USER NOT FOUND"), 404
        result = self.build_user_dict(user)
        return jsonify(User=result), 200
    def deleteUser(self, uid):
        return jsonify(DeleteStatus="OK"), 200
'''