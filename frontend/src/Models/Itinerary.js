var Itinerary = (data) => {
    return {
        name: "Itinerary",
        columns: [
            {
                Header: "ID",
                accessor: "id",
            },
            {
                Header: "Date",
                accessor: "date",
            },
            {
                Header: "Start Time",
                accessor: "start_time",
            },
            {
                Header: "End Time",
                accessor: "end_time",
            },
            {
                Header: "Driver ID",
                accessor: "driver_id",
            },
            {
                Header: "Trolley ID",
                accessor: "trolley_id",
            },
            {
                Header: "Route ID",
                accessor: "route_id",
            },
        ],
        data: data
    }
}

export default Itinerary;