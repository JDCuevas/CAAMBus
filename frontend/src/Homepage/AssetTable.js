import React from 'react';
import ReactTable from "react-table";
import 'react-table/react-table.css'

export default class AssetTable extends React.Component {
    render() {
        return (
            <div>
                <h2>{this.props.name}</h2>
                <ReactTable
                    data={this.props.data}
                    columns={this.props.columns}
                />
            </div>
        )
    }
}