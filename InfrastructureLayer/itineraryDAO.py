import csv
from config.dbconfig import pg_config
import psycopg2

class ItineraryDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id

    def getAllItineraries(self):
        cursor = self.conn.cursor()
        query = "select * from Itineraries;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getItineraryById(self, itinerary_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Itineraries WHERE itinerary_id = %s;"
        cursor.execute(query, (itinerary_id,))
        
        result = cursor.fetchone()

        return result

    def getItinerariesByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from Itineraries where date = %s;"
        cursor.execute(query, (date,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getItinerariesByStartTime(self, start_time):
        cursor = self.conn.cursor()
        query = "select * from Itineraries where start_time = %s;"
        cursor.execute(query, (start_time,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getItinerariesByEndTime(self, end_time):
        cursor = self.conn.cursor()
        query = "select * from Itineraries where end_time = %s;"
        cursor.execute(query, (end_time,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getItinerariesByDriverId(self, driver_id):
        cursor = self.conn.cursor()
        query = "select * from Itineraries where driver_id = %s;"
        cursor.execute(query, (driver_id,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getItinerariesByTrolleyId(self, trolley_id):
        cursor = self.conn.cursor()
        query = "select * from Itineraries where trolley_id = %s;"
        cursor.execute(query, (trolley_id,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getItinerariesByRouteId(self, route_id):
        cursor = self.conn.cursor()
        query = "select * from Itineraries where route_id = %s;"
        cursor.execute(query, (route_id,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getFullItineraryDetails(self, itinerary_id):
        cursor = self.conn.cursor()
        query = '''SELECT * 
                   FROM Itineraries natural inner join Drivers natural inner join Trolleys natural inner join Routes
                   WHERE itinerary_id = %s'''
        cursor.execute(query, (itinerary_id,))
        
        result = cursor.fetchone()

        return result


    def insert(self, date, start_time, end_time, driver_id, trolley_id, route_id):
        cursor = self.conn.cursor()
        query = "insert into Itineraries(date, start_time, end_time, driver_id, trolley_id, route_id) values (%s, %s, %s, %s, %s, %s) returning itinerary_id;"
        cursor.execute(query, (date, start_time, end_time, driver_id, trolley_id, route_id,))
        itinerary_id = cursor.fetchone()[0]
        self.conn.commit()

        return itinerary_id

    def delete(self, itinerary_id):
        cursor = self.conn.cursor()
        query = "delete from Drivers where itinerary_id = %s;"
        cursor.execute(query, (itinerary_id,))
        self.conn.commit()

        return itinerary_id

    def update(self, itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id):
        cursor = self.conn.cursor()
        query = "update Itineraries set date = %s, start_time = %s, end_time = %s, driver_id = %s, trolley_id = %s, route_id = %s where itinerary_id = %s;"
        cursor.execute(query, (date, start_time, end_time, driver_id, trolley_id, route_id, itinerary_id,))
        self.conn.commit()

        return itinerary_id
