import React, { Component } from 'react';
import AssetTable from './AssetTable';

export default class Homepage extends Component {
    render() {
        return (
            <div className="Homepage">
                <AssetTable />
                <AssetTable />
                <AssetTable />
                <AssetTable />
            </div>
        )
    }
}