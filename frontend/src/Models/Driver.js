var Driver = function(data) {
    return {
        name: "Drivers",
        columns: [
            {
                Header: "ID",
                accessor: "driver_id",
            },
            {
                Header: "First Name",
                accessor: "first_name",
            },
            {
                Header: "Last Name",
                accessor: "last_name",
            },
            {
                Header: "License",
                accessor: "license",
            },
            {
                Header: "Phone Number",
                accessor: "phone",
            },
        ],
        data: data
    }
}

export default Driver