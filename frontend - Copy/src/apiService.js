import axios from 'axios'

// axios.defaults.headers.common = {
//     "X-Goog-Authenticated-User-Email": "accounts.google.com:teuschler.c@pg.com",
// };


const axiosConfig = {
    baseURL: 'http://api:8686',
    timeout: 30000,
    // Dev config
    // headers:{"X-Goog-Authenticated-User-Email": process.env.VUE_APP_LOGGED_IN_DEV_ACCOUNT }
};

// console.log('api_base_url: ' + api_base_url)

var apiService = axios.create(axiosConfig);

export default {
    getSeason(year) {
        return apiService.get(`/season/${year.toString()}`).then((data) =>{
            return data
        })
    },

    getHelloWorld() {
        return apiService.get('/').then((data) => {
            return data
        })
    }
}