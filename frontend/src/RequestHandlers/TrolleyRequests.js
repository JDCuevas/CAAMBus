import axios from 'axios'

const url = 'http://127.0.0.1:5000/CAAMBus/trolleys'

const TrolleyRequests = {
    getAllTrolleys: async () => {
        return axios.get(`${url}`).then(
            (res) => {return res.data.Trolleys}
        ).catch(err => {/* TODO */});
    }
}

export default TrolleyRequests;