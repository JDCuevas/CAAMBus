from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from ApplicationLayer.driverHandler import DriverHandler
from ApplicationLayer.trolleyHandler import TrolleyHandler
from ApplicationLayer.routeHandler import RouteHandler
from ApplicationLayer.itineraryHandler import ItineraryHandler


app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True # Debug Mode. Server is reloaded on any code change
                           # and provides detailed error messages.
app.config['JSON_SORT_KEYS'] = False

@app.route('/CAAMBus/')  # OK
def home():
    return "Welcome to CAAMBus!"

###################### Drivers ######################
'''
@app.route('/CAAMBus/register', methods=['POST'])
def register():
    if request.method =='POST':
        return DriverHandler().insertDriver()

@app.route('/CAAMBus/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # return DriverHandler().getItineraries(request.get_json('data'))
        return DriverHandler().getItineraries()
'''

@app.route('/CAAMBus/drivers', methods=['GET'])
def getAllDrivers():
    if request.method == 'GET':
        return DriverHandler().getAllDrivers()

@app.route('/CAAMBus/drivers/<int:driver_id>', methods=['GET'])
def getDriverById(driver_id):
    if request.method == 'GET':
        return DriverHandler().getDriverById(driver_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/CAAMBus/drivers/first_name/<string:first_name>', methods=['GET'])
def getDriversByFirstName(first_name):
    if request.method == 'GET':
        return DriverHandler().getDriversByFirstName(first_name)

@app.route('/CAAMBus/drivers/last_name/<string:last_name>', methods=['GET'])
def getDriversByLastName(last_name):
    if request.method == 'GET':
        return DriverHandler().getDriversByLastName(last_name)

@app.route('/CAAMBus/drivers/name/<string:first_name>+<string:last_name>', methods=['GET'])
def getDriverByName(first_name, last_name):
    if request.method == 'GET':
        return DriverHandler().getDriversByName(first_name, last_name)

@app.route('/CAAMBus/drivers/license/<int:license>', methods=['GET'])
def getDriverByLicense(license):
    if request.method == 'GET':
        return DriverHandler().getDriverByLicense(license)

@app.route('/CAAMBus/drivers/phone/<int:phone>', methods=['GET'])
def getDriverContacts(phone):
    if request.method == 'GET':
        return DriverHandler().getDriverByPhone(phone)

###################### Trolleys ######################

@app.route('/CAAMBus/trolleys', methods=['GET'])
def getAllTrolleys():
    if request.method == 'GET':
        return TrolleyHandler().getAllTrolleys()

@app.route('/CAAMBus/trolleys/<int:trolley_id>', methods=['GET'])
def getTrolleyById(trolley_id):
    if request.method == 'GET':
        return TrolleyHandler().getTrolleyById(trolley_id)

@app.route('/CAAMBus/trolleys/plate/<string:plate>', methods=['GET'])
def getTrolleyByPlate(plate):
    if request.method == 'GET':
        return TrolleyHandler().getTrolleyByPlate(plate)

@app.route('/CAAMBus/trolleys/capacity/<int:capacity>', methods=['GET'])
def getTrolleysByCapacity(capacity):
    if request.method == 'GET':
        return TrolleyHandler().getTrolleysByCapacity(capacity)

@app.route('/CAAMBus/trolleys/mileage/<float:mileage_low>-<float:mileage_high>', methods=['GET'])
def getTrolleysByMileageRange(mileage_low, mileage_high):
    if request.method == 'GET':
        return TrolleyHandler().getTrolleysByMileageRange(mileage_low, mileage_high)


###################### Routes ######################

@app.route('/CAAMBus/routes', methods=['GET'])
def getAllRoutes():
    if request.method == 'GET':
        return RouteHandler().getAllRoutes()

@app.route('/CAAMBus/routes/<int:route_id>', methods=['GET'])
def getRouteById(route_id):
    if request.method == 'GET':
        return RouteHandler().getRouteById(route_id)

@app.route('/CAAMBus/routes/name/<string:route_name>', methods=['GET'])
def getRouteByName(route_name):
    if request.method == 'GET':
        return RouteHandler().getRouteByName(route_name)

@app.route('/CAAMBus/routes/<int:route_id>/stops/', methods=['GET'])
def getRouteStops(route_id):
    if request.method == 'GET':
        return RouteHandler().getRouteStops(route_id)

@app.route('/CAAMBus/routes/stops/<int:stop_id>', methods=['GET'])
def getStopById(stop_id):
    if request.method == 'GET':
        return RouteHandler().getStopById(stop_id)

###################### Itineraries ######################

@app.route('/CAAMBus/itineraries', methods=['GET'])
def getAllItineraries():
    if request.method == 'GET':
        return ItineraryHandler().getAllItineraries()

@app.route('/CAAMBus/itineraries/<int:itinerary_id>', methods=['GET'])
def getItineraryById(itinerary_id):
    if request.method == 'GET':
        return ItineraryHandler().getItineraryById(itinerary_id)

@app.route('/CAAMBus/itineraries/date/<string:date>', methods=['GET'])
def getItinerariesByDate(date):
    if request.method == 'GET':
        return ItineraryHandler().getItinerariesByDate(date)

@app.route('/CAAMBus/itineraries/start_time/<string:start_time>', methods=['GET'])
def getItinerariesByStartTime(start_time):
    if request.method == 'GET':
        return ItineraryHandler().getItinerariesByStartTime(start_time)

@app.route('/CAAMBus/itineraries/end_time/<string:end_time>', methods=['GET'])
def getItinerariesByEndTime(end_time):
    if request.method == 'GET':
        return ItineraryHandler().getItinerariesByEndTime(end_time)

@app.route('/CAAMBus/itineraries/driver/<int:driver_id>', methods=['GET'])
def getItinerariesByDriverId(driver_id):
    if request.method == 'GET':
        return ItineraryHandler().getItinerariesByDriverId(driver_id)

@app.route('/CAAMBus/itineraries/trolley/<int:trolley_id>', methods=['GET'])
def getItinerariesByTrolleyId(trolley_id):
    if request.method == 'GET':
        return ItineraryHandler().getItinerariesByTrolleyId(trolley_id)

@app.route('/CAAMBus/itineraries/route/<int:route_id>', methods=['GET'])
def getItineraryByRouteId(route_id):
    if request.method == 'GET':
        return ItineraryHandler().getItineraryById(route_id)

@app.route('/CAAMBus/itineraries/<int:itinerary_id>/all', methods=['GET'])
def getFullItineraryDetails(itinerary_id):
    if request.method == 'GET':
        return ItineraryHandler().getFullItineraryDetails(itinerary_id)

if __name__ == '__main__':
    app.run()
