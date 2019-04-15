import React, { Component } from 'react';
import Homepage from './Homepage/Homepage'
import Navbar from './Navbar';
import './App.css';


export default class App extends Component {
  render() {
    return (
      <div className="App">
        <Navbar />
        <Homepage />
      </div>
    );
  }
}


