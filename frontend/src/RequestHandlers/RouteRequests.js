import axios from 'axios'

const url = 'http://127.0.0.1:5000/CAAMBus/routes'

const RoutesRequests = {
    getAllIRoutes: async () => {
        return axios.get(`${url}`).then(
            (res) => {return res.data.Routes}
        ).catch(err => {/* TODO */});
    }
}

export default RoutesRequests;