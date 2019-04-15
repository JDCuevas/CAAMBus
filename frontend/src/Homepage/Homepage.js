import React, { Component } from 'react';
import AssetTable from './AssetTable';
import Driver from '../Models/Driver';
import Itinerary from '../Models/Itinerary';
import DriverRequests from '../RequestHandlers/DriverRequests';
import Trolley from '../Models/Trolley';
import Route from '../Models/Route';
import ItineraryRequests from '../RequestHandlers/ItineraryRequests';
import TrolleyRequests from '../RequestHandlers/TrolleyRequests';
import RoutesRequests from '../RequestHandlers/RouteRequests';

export default class Homepage extends Component {
    constructor() {
        super();
    }

    componentDidMount() {
        var promises = [
            ItineraryRequests.getAllItineraries(),
            DriverRequests.getAllDrivers(),
            TrolleyRequests.getAllTrolleys(),
            RoutesRequests.getAllIRoutes()
        ];

        Promise.all(promises).then(
            data => {
                console.log(data);
                this.setState({
                    //setup table
                    itinerary: Itinerary(data[0]),
                    driver: Driver(data[1]),
                    trolley: Trolley(data[2]),
                    route: Route(data[3])
                });
            }
        )
    }

    render() {
        if (!this.state) return null;
        return (
            <div className="Homepage">
                <AssetTable name={this.state.itinerary.name}
                    columns={this.state.itinerary.columns}
                    data={this.state.itinerary.data} />

                <AssetTable name={this.state.driver.name}
                    columns={this.state.driver.columns}
                    data={this.state.driver.data} />

                <AssetTable name={this.state.trolley.name}
                    columns={this.state.trolley.columns}
                    data={this.state.trolley.data} />

                <AssetTable name={this.state.route.name}
                    columns={this.state.route.columns}
                    data={this.state.route.data} />
            </div>
        )
    }
}