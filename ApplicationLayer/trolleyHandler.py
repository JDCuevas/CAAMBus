from flask import jsonify
from InfrastructureLayer.trolleyDAO import TrolleyDao


class TrolleyHandler:
    # Schema: trolley_id, plate, capacity, mileage

    def build_trolley_dict(self, row):
        result = {}
        result['trolley_id'] = row[0]
        result['plate'] = row[1]
        result['capacity'] = row[2]
        result['mileage'] = row[3]

        return result

    # Gets
    def getAllTrolleys(self):
        dao = TrolleyDao()
        result_list = dao.getAllTrolleys()
        trolleys_list = []

        for row in result_list:
            result = self.build_trolley_dict(row)
            trolleys_list.append(result)

        return jsonify(Trolleys=trolleys_list)

    def getTrolleyById(self, trolley_id):
        dao = TrolleyDao()
        row = dao.getTrolleyById(trolley_id)

        if not row:
            return jsonify(Error="Trolley Not Found"), 404
        else:
            trolley = self.build_trolley_dict(row)
            return jsonify(Trolley=trolley)

    def getTrolleyByPlate(self, plate):
        dao = TrolleyDao()
        row = dao.getTrolleyByPlate(plate)

        if not row:
            return jsonify(Error="Trolley Not Found"), 404
        else:
            trolley = self.build_trolley_dict(row)
            return jsonify(Trolley=trolley)

    def getTrolleysByCapacity(self, capacity):
        dao = TrolleyDao()
        result_list = dao.getTrolleysByCapacity(capacity)
        trolleys_list = []

        if not result_list:
            return jsonify(Error="Trolleys Not Found"), 404
        else:
            for row in result_list:
                result = self.build_trolley_dict(row)
                trolleys_list.append(result)
            return jsonify(Trolleys=trolleys_list)

    # Whats the use for this? Better to specify a range
    def getTrolleysByMileageRange(self, mileage_low, mileage_high):
        dao = TrolleyDao()
        result_list = dao.getTrolleysByMileageRange(mileage_low, mileage_high)
        trolleys_list = []

        if not result_list:
            return jsonify(Error="Trolleys Not Found"), 404
        else:
            for row in result_list:
                result = self.build_trolley_dict(row)
                trolleys_list.append(result)
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

