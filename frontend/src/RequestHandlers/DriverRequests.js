import axios from 'axios';

const url = 'http://127.0.0.1:5000/CAAMBus/drivers'

const DriverRequests = {
    getAllDrivers: async () => {
        return axios.get(`${url}`).then(
            (res) => {return res.data.Driver}
        ).catch(err => {/* TODO */});
    }
}

export default DriverRequests;