import axios from 'axios';

class CrudService {
    constructor(namespace) {
        this.namespace = namespace;
        // set global axios defaults
        axios.defaults.baseURL = 'http://localhost:5000';
        axios.defaults.headers.post['Content-Type'] = 'application/json';
        // if (cookie.get('token')) axios.defaults.headers.common['Authorization'] = cookie.get('token');
    }

    find = (params) => {
        return axios.get(this.namespace, { params });
    };

    get = (id, params) => {
        return axios.get(`${this.namespace}/${id}`, { params });
    };

    create = (data, params) => {
        return axios.post(this.namespace, data, { params });
    };

    update = (id, data, params) => {
        return axios.put(`${this.namespace}/${id}`, data, { params });
    };

    patch = (id, data, params) => {
        return axios.patch(`${this.namespace}/${id}`, data, { params });
    };

    remove = (id, params) => {
        return axios.delete(`${this.namespace}/${id}`, { params });
    };
}

export default CrudService;
