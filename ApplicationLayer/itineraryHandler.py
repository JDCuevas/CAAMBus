from flask import jsonify
from InfrastructureLayer.itineraryDAO import ItineraryDao
from DomainLayer.itinerary import Itinerary

class ItineraryHandler:
    # Schema: itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id
    dao = ItineraryDao()

    # Gets
    def getAllItineraries(self):
        result_list = self.dao.getAllItineraries()
        itinerary_list = []

        for row in result_list:
            itinerary = Itinerary(row)
            result = itinerary.itineraryInfo()
            itinerary_list.append(result)

        print(itinerary_list)

        return jsonify(Itineraries=itinerary_list)


    def getItineraryById(self, itinerary_id):
        result = self.dao.getItineraryById(itinerary_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = Itinerary(result)
            itinerary = itinerary.itineraryInfo()
            return jsonify(Itinerary=itinerary)

    def getItinerariesByDate(self, date):
        result_list = self.dao.getItinerariesByDate(date)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                itinerary = Itinerary(row)
                result = itinerary.itineraryInfo()
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByStartTime(self, start_time):
        result_list = self.dao.getItinerariesByStartTime(start_time)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                itinerary = Itinerary(row)
                result = itinerary.itineraryInfo()
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByEndTime(self, end_time):
        result_list = self.dao.getItinerariesByEndTime(end_time)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                itinerary = Itinerary(row)
                result = itinerary.itineraryInfo()
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByDriverId(self, driver_id):
        result_list = self.dao.getItinerariesByDriverId(driver_id)
        itinerary_list = []

        if not result_list:
            return jsonify(Error="Itineraries Not Found"), 404
        else:
            for row in result_list:
                itinerary = Itinerary(row)
                result = itinerary.itineraryInfo()
                itinerary_list.append(result)
            return jsonify(Itineraries=itinerary_list)

    def getItinerariesByTrolleyId(self, trolley_id):
        result = self.dao.getItinerariesByTrolleyId(trolley_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = Itinerary(result)
            itinerary = itinerary.itineraryInfo()
            return jsonify(Itinerary=itinerary)

    def getItinerariesByRouteId(self, route_id):
        result = self.dao.getItinerariesByRouteId(route_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = Itinerary(result)
            itinerary = itinerary.itineraryInfo()
            return jsonify(Itinerary=itinerary)

    def getFullItineraryDetails(self, itinerary_id):
        result = self.dao.getFullItineraryDetails(itinerary_id)

        if not result:
            return jsonify(Error="Itinerary Not Found"), 404
        else:
            itinerary = Itinerary(result)
            itinerary = itinerary.itineraryInfo()
            return jsonify(Itinerary=itinerary)

'''
    # CRUDS
    def insertUser(self):
        user = self.dao.insertUser()
        return jsonify(User=user), 201
    def updateUser(self, uid, form):
        user = self.dao.update(uid)
        if not user:
            return jsonify(Error="USER NOT FOUND"), 404
        result = self.build_user_dict(user)
        return jsonify(User=result), 200
    def deleteUser(self, uid):
        return jsonify(DeleteStatus="OK"), 200
'''