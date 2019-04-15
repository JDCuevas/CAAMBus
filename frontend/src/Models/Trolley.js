var Trolley = function(data) {
    return {
        name: "Trolleys",
        columns: [
            {
                Header: "ID",
                accessor: "trolley_id",
            },
            {
                Header: "License Plate",
                accessor: "plate",
            },
            {
                Header: "Capacity Limit",
                accessor: "capacity",
            },
            {
                Header: "mileage",
                accessor: "mileage",
            },
        ],
        data: data
    }
}

export default Trolley;