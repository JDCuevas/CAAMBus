import axios from 'axios'

const url = 'http://127.0.0.1:5000/CAAMBus/itineraries'

const ItineraryRequests = {
    getAllItineraries: async () => {
        return axios.get(`${url}`).then(
            (res) => {return res.data.Itineraries}
        ).catch(err => {/* TODO */});
    }
}

export default ItineraryRequests;