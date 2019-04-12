

CREATE TABLE Drivers (
driver_id serial PRIMARY KEY,
first_name varchar(20),
last_name varchar(20),
license bigint,
phone bigint);

INSERT INTO Drivers (first_name, last_name, license, phone) VALUES
('Julian', 'Cuevas', 6523031, 7876074678),
('Raul', 'Mojica', 6523231, 7875434237);


CREATE TABLE Routes 
(route_id serial PRIMARY KEY, route_name varchar(25));

CREATE TABLE Stops
(stop_id SERIAL PRIMARY KEY, stop_name varchar(25), latitude float, longitude foat);

CREATE TABLE StopsInRoutes 
(route_id integer REFERENCES Routes(route_id), stop_id integer REFERENCES Stopsstop_id), primary key (route_id, stop_id));

CREATE TABLE Trolleys 
(trolley_id SERIAL PRIMARY KEY, plate varchar(8), capacity integer, mileage float);

CREATE TABLE Itineraries
(itinerary_id SERIAL PRIMARY KEY, date TIMESTAMPTZ, start_time TIMESTAMPTZ, end_time TIMESTAMPTZ, driver_id integer references Drivers(driver_id), trolley_id integer references Trolleys(trolley_id), route_id integer references Routes(route_id));