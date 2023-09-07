import axios from "axios";

const IP="172.16.4.33"
const URL = import.meta.env.VITE_API || `http://${IP}:8008`;
const endpoint = URL + "/api/movements";

export const fetchMovements = () => axios.get(endpoint);

// export const fetchTask = (id) => axios.get(`${endpoint}/${id}`);

// export const createTask = (task) => axios.post(endpoint, task);

// export const updateTask = (id, task) => axios.put(`${endpoint}/${id}`, task);

// export const deleteTask = (id) => axios.delete(`${endpoint}/${id}`);