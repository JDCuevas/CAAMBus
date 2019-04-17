from flask import jsonify
from InfrastructureLayer.driverDAO import DriverDao
from DomainLayer.driver import Driver, driverFactory, driverRepository


class DriverHandler:
    # Schema: driver_id, first_name, last_name, license, phone

    # Gets
    def getAllDrivers(self):
        dao = DriverDao()
        results_list = dao.getAllDrivers()
        drivers_list = []

        drivers_list = driverRepository(results_list)

        return jsonify(Driver=drivers_list)

    def getDriverById(self, driver_id):
        dao = DriverDao()
        result = dao.getDriverById(driver_id)

        if not result:
            return jsonify(Error="Driver Not Found"), 404
        else:
            ddriver = driverRepository(result)
            return jsonify(Driver=driver)

    def getDriversByFirstName(self, first_name):
        dao = DriverDao()
        results_list = dao.getDriversByFirstName(first_name)
        drivers_list = []

        if not results_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            drivers_list = driverRepository(results_list)
            return jsonify(Driver=drivers_list)

    def getDriversByLastName(self, last_name):
        dao = DriverDao()
        results_list = dao.getDriversByLastName(last_name)
        drivers_list = []

        if not results_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            drivers_list = driverRepository(results_list)
            return jsonify(Driver=drivers_list)

        return jsonify(Driver=drivers_list)

    def getDriversByName(self, first_name, last_name):
        dao = DriverDao()
        results_list = dao.getDriversByName(first_name, last_name)
        drivers_list = []

        if not results_list:
            return jsonify(Error="Drivers Not Found"), 404
        else:
            drivers_list = driverRepository(results_list)
            return jsonify(Drivers=drivers_list)

    def getDriverByLicense(self, license):
        dao = DriverDao()
        result = dao.getDriverByLicense(license)
        
        if not result:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = driverRepository(result)
            return jsonify(Driver=driver)

    def getDriverByPhone(self, phone):
        dao = DriverDao()
        result = dao.getDriverByPhone(phone)

        if not result:
            return jsonify(Error="Driver Not Found"), 404
        else:
            driver = driverRepository(result)
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