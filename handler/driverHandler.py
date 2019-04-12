from flask import jsonify
from dao.driverDAO import DriverDao


class DriverHandler:
    # Schema: driver_id, first_name, last_name, license, phone

    def build_driver_dict(self, row):
        result = {}
        result['driver_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['license'] = row[3]
        result['phone'] = row[4]

        return result

    # Gets
    def getAllDrivers(self):
        dao = DriverDao()
        result_list = dao.getAllDrivers()
        driver_list = []

        for row in result_list:
            result = self.build_driver_dict(row)
            driver_list.append(result)

        return jsonify(Driver=driver_list)

    def getDriverById(self, driver_id):
        dao = DriverDao()
        row = dao.getDriverById(driver_id)

        if not row:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = self. build_driver_dict(row)
            return jsonify(Driver=driver)

    def getDriversByFirstName(self, first_name):
        dao = DriverDao()
        driver_list = dao.getDriversByFirstName(first_name)
        result_list = []

        if not driver_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            for row in driver_list:
                result = self.build_driver_dict(row)
                result_list.append(result)
            return jsonify(Driver=result_list)

    def getDriversByLastName(self, last_name):
        dao = DriverDao()
        driver_list = dao.getDriversByLastName(last_name)
        result_list = []

        if not driver_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            for row in driver_list:
                result = self.build_driver_dict(row)
                result_list.append(result)
            return jsonify(Driver=result_list)

        return jsonify(Driver=driver_list)

    def getDriversByName(self, first_name, last_name):
        dao = DriverDao()
        driver_list = dao.getDriversByName(first_name, last_name)
        result_list = []

        if not driver_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            for row in driver_list:
                result = self.build_driver_dict(row)
                result_list.append(result)
            return jsonify(Drivers=result_list)

    def getDriverByLicense(self, license):
        dao = DriverDao()
        row = dao.getDriverByLicense(license)
        
        if '@' not in license:
            return jsonify(Error="Not A Valid License"), 404
        elif not row:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = self. build_driver_dict(row)
            return jsonify(Driver=driver)

    def getDriverByPhone(self, phone):
        dao = DriverDao()
        row = dao.getDriverByPhone(phone)
        
        if '@' not in phone:
            return jsonify(Error="Not A Valid Phone Number"), 404
        elif not row:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = self. build_driver_dict(row)
            return jsonify(Driver=driver)

'''
    # CRUDS
    def insertDriver(self):
        dao = DriverDao()
        driver = dao.insertDriver()

        return jsonify(Driver=driver), 201

    def updateDriver(self, driver_id, form):
        dao = DriverDao()
        driver = dao.update(driver_id)
        if not driver:
            return jsonify(Error="USER NOT FOUND"), 404

        result = self.build_driver_dict(driver)
        return jsonify(Driver=result), 200

    def deleteDriver(self, driver_id):
        return jsonify(DeleteStatus="OK"), 200
'''