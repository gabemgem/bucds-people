import axios from "axios";

const http = axios.create({
    baseURL: 'localhost'
});

export default http;