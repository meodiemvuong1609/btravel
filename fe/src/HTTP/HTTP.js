import axios from 'axios';

const HTTP = axios.create({
    // baseURL: 'http://localhost:8000/',
    baseURL: 'http://123.17.221.223:8000/',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': localStorage.getItem('token')?`Token ${localStorage.getItem('token')}`:undefined
    }
});

export default HTTP;
