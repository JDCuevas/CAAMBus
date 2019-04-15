var Route = function(data) {
   return {
        name: "Routes",
        columns: [
            {
                Header: "ID",
                accessor: "route_id",
            },
            {
                Header: "Route Name",
                accessor: "name",
            },
        ],
        data: data
    }
}

export default Route;