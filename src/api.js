import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:8000/api' });

export const fetchScores = () => API.get('/scores');
export const createScore = (score) => API.post('/scores', score);
export const login = (user) => API.post('/auth/login', user);
export const signup = (user) => API.post('/auth/signup', user);
