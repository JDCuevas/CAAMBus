from flask import jsonify
from InfrastructureLayer.driverDAO import DriverDao
from DomainLayer.driver import Driver


class DriverHandler:
    # Schema: driver_id, first_name, last_name, license, phone
    
    # Gets
    def getAllDrivers(self):
        dao = DriverDao()
        driver_list = dao.getAllDrivers()
        result_list = []

        for row in driver_list:
            driver = Driver(row)
            result = driver.driverInfo()
            result_list.append(result)

        return jsonify(Driver=result_list)

    def getDriverById(self, driver_id):
        dao = DriverDao()
        row = dao.getDriverById(driver_id)

        if not row:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = Driver(row)
            driver = driver.driverInfo()
            return jsonify(Driver=driver)

    def getDriversByFirstName(self, first_name):
        dao = DriverDao()
        driver_list = dao.getDriversByFirstName(first_name)
        result_list = []

        if not driver_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            for row in driver_list:
                driver = Driver(row)
                result = driver.driverInfo()
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
                driver = Driver(row)
                result = driver.driverInfo()
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
                driver = Driver(row)
                result = driver.driverInfo()
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
            driver = Driver(row)
            driver = driver.driverInfo()
            return jsonify(Driver=driver)

    def getDriverByPhone(self, phone):
        dao = DriverDao()
        row = dao.getDriverByPhone(phone)
        
        if '@' not in phone:
            return jsonify(Error="Not A Valid Phone Number"), 404
        elif not row:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = Driver(row)
            driver = driver.driverInfo()
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
d
    def deleteDriver(self, driver_id):
        return jsonify(DeleteStatus="OK"), 200
'''