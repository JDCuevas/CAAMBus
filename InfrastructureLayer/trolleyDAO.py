import csv
from config.dbconfig import pg_config
import psycopg2

class TrolleyDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: trolley_id, plate, capacity, mileage

    def getAllTrolleys(self):
        cursor = self.conn.cursor()
        query = "select * from Trolleys;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getTrolleyById(self, trolley_id):
        cursor = self.conn.cursor()
        query = "select * from Trolleys where trolley_id = %s;"
        cursor.execute(query, (trolley_id,))

        result = cursor.fetchone()

        return result

    def getTrolleyByPlate(self, plate):
        cursor = self.conn.cursor()
        query = "select * from Trolleys where plate = %s;"
        cursor.execute(query, (plate,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getTrolleysByCapacity(self, capacity):
        cursor = self.conn.cursor()
        query = "select * from Trolleys where capacity = %s;"
        cursor.execute(query, (capacity,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getTrolleysByMileageRange(self, mileage_low, mileage_high):
        cursor = self.conn.cursor()
        query = "select * from Trolleys where mileage >= %s and mileage <= %s;"
        cursor.execute(query, (mileage_low, mileage_high,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def insert(self, plate, capacity, mileage):
        cursor = self.conn.cursor()
        query = "insert into Trolleys(plate, capacity, mileage) values (%s, %s, %s) returning trolley_id;"
        cursor.execute(query, (plate, capacity, mileage,))
        trolley_id = cursor.fetchone()[0]
        self.conn.commit()

        return trolley_id

    def delete(self, trolley_id):
        cursor = self.conn.cursor()
        query = "delete from Trolleys where trolley_id = %s;"
        cursor.execute(query, (trolley_id,))
        self.conn.commit()

        return trolley_id

    def update(self, trolley_id, plate, capacity, mileage):
        cursor = self.conn.cursor()
        query = "update Trolleys set plate = %s, capacity = %s, mileage = %s where trolley_id = %s;"
        cursor.execute(query, (plate, capacity, mileage, trolley_id,))
        self.conn.commit()
        
        return trolley_id