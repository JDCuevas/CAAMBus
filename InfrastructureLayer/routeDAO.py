import csv
from config.dbconfig import pg_config
import psycopg2

class RouteDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: 
    # Routes: route_id, route_name
    # Stops: stop_id, stop_name, latitude, longitude
    # StopsInRoutes: route_id, stop_id, primary key(route_id, stop_id)

    def getAllRoutes(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Routes;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getRouteById(self, route_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Routes WHERE route_id = %s;"
        cursor.execute(query, (route_id,))
        
        result = cursor.fetchone()

        return result

    def getRouteByName(self, route_name):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Routes WHERE route_name = %s;"
        cursor.execute(query, (route_name,))
        
        result = cursor.fetchone()

        return result

    def getRouteStops(self, route_id):
        cursor = self.conn.cursor()
        query = '''SELECT route_id, route_name, stop_id, stop_name, latitude, longitude 
                   FROM Routes natural inner join StopsInRoutes natural inner join Stops
                   ORDER BY route_id, stop_id;'''
        cursor.execute(query, (route_id,))
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getStopById(self, stop_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Stops WHERE stop_id = %s;"
        cursor.execute(query, (stop_id,))
        
        result = cursor.fetchone()

        return result

    def insert(self, route_name):
        cursor = self.conn.cursor()
        query = "insert into Routes(route_name) values (%s) returning route_id;"
        cursor.execute(query, (route_name,))
        route_id = cursor.fetchone()[0]
        self.conn.commit()

        return route_id

    def delete(self, route_id):
        cursor = self.conn.cursor()
        query = "delete from Routes where route_id = %s;"
        cursor.execute(query, (route_id,))
        self.conn.commit()

        return route_id

    def update(self, route_id, route_name):
        cursor = self.conn.cursor()
        query = "update Routes set route_name = %s where route_id = %s;"
        cursor.execute(query, (route_name, route_id,))
        self.conn.commit()
        
        return route_id