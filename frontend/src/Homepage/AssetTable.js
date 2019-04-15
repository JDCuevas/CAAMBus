import React from 'react';
import ReactTable from "react-table";

export default class AssetTable extends React.Component {
    render() {
        return (
            <div>
                <h2>{this.props.asset}</h2>
                <ReactTable
                    data={this.props.data}
                    columns={this.props.columns}
                />
            </div>
        )
    }
}