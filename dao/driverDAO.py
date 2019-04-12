import csv
from config.dbconfig import pg_config
import psycopg2

class DriverDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: driver_id, first_name, last_name, license, phone

    def getAllDrivers(self):
        cursor = self.conn.cursor()
        query = "select * from Drivers;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getDriverById(self, driver_id):
        cursor = self.conn.cursor()
        query = "select * from Drivers where driver_id = %s;"
        cursor.execute(query, (driver_id,))

        result = cursor.fetchone()

        return result

    def getDriversByFirstName(self, first_name):
        cursor = self.conn.cursor()
        query = "select * from Drivers where first_name = %s;"
        cursor.execute(query, (first_name,))
        result = []

        for row in cursor:
                result.append(row)

        return result

    def getDriversByLastName(self, last_name):
        cursor = self.conn.cursor()
        query = "select * from Drivers where last_name = %s;"
        cursor.execute(query, (last_name,))
        result = []

        for row in cursor:
                result.append(row)

        return result

    def getDriversByName(self, first_name, last_name):
        cursor = self.conn.cursor()
        query = "select * from Drivers where first_name = %s and last_name = %s;"
        cursor.execute(query, (first_name,last_name,))
        result = []

        for row in cursor:
                result.append(row)

        return result

    def getDriverByLicense(self, license):
        cursor = self.conn.cursor()
        query = "select * from Drivers where license = %s;"
        cursor.execute(query, (license,))
        result = cursor.fetchone()

        return result

    def getDriverByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "select * from Drivers where phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()

        return result

    def insert(self, first_name, last_name, license, phone):
        cursor = self.conn.cursor()
        query = "insert into Drivers(first_name, last_name, license, phone) values (%s, %s, %s, %s) returning driver_id;"
        cursor.execute(query, (first_name, last_name, license, phone,))
        driver_id = cursor.fetchone()[0]
        self.conn.commit()

        return driver_id

    def delete(self, driver_id):
        cursor = self.conn.cursor()
        query = "delete from Drivers where driver_id = %s;"
        cursor.execute(query, (driver_id,))
        self.conn.commit()

        return driver_id

    def update(self, driver_id, first_name, last_name, license, phone):
        cursor = self.conn.cursor()
        query = "update Drivers set first_name = %s, last_name = %s, license = %s, phone = %s where driver_id = %s;"
        cursor.execute(query, (first_name, last_name, license, phone, driver_id,))
        self.conn.commit()
        
        return driver_id