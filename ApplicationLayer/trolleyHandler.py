from flask import jsonify
from InfrastructureLayer.trolleyDAO import TrolleyDao
from DomainLayer.trolley import Trolley, trolleyFactory, trolleyRepository, getInfo


class TrolleyHandler:
    # Schema: trolley_id, plate, capacity, mileage
    # Gets
    
    def getAllTrolleys(self):
        dao = TrolleyDao()
        results_list = dao.getAllTrolleys()
        trolleys_list = []

        trolleys_list = trolleyRepository(results_list)
        trolleys_list = list(map(getInfo, trolleys_list))

        return jsonify(Trolleys=trolleys_list)

    def getTrolleyById(self, trolley_id):
        dao = TrolleyDao()
        result = dao.getTrolleyById(trolley_id)

        if not result:
            return jsonify(Error="Trolley Not Found"), 404
        else:
            trolley = trolleyRepository(result)
            trolley = getInfo(trolley)
            return jsonify(Trolley=trolley)

    def getTrolleyByPlate(self, plate):
        dao = TrolleyDao()
        result = dao.getTrolleyByPlate(plate)

        if not result:
            return jsonify(Error="Trolley Not Found"), 404
        else:
            trolley = trolleyRepository(result)
            trolley = getInfo(trolley)
            return jsonify(Trolley=trolley)

    def getTrolleysByCapacity(self, capacity):
        dao = TrolleyDao()
        results_list = dao.getTrolleysByCapacity(capacity)
        trolleys_list = []

        if not results_list:
            return jsonify(Error="Trolleys Not Found"), 404
        else:
            trolleys_list = trolleyRepository(results_list)
            trolleys_list = list(map(getInfo, trolleys_list))
            return jsonify(Trolleys=trolleys_list)

    # Whats the use for this? Better to specify a range
    def getTrolleysByMileageRange(self, mileage_low, mileage_high):
        dao = TrolleyDao()
        results_list = dao.getTrolleysByMileageRange(mileage_low, mileage_high)
        trolleys_list = []

        if not results_list:
            return jsonify(Error="Trolleys Not Found"), 404
        else:
            trolleys_list = trolleyRepository(results_list)
            trolleys_list = list(map(getInfo, trolleys_list))
            return jsonify(Trolleys=trolleys_list)
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

