import axios from 'axios';
import toast from 'react-hot-toast';
const api = axios.create({
  baseURL: 'http://localhost:8080',
});

api.interceptors.response.use(
  (response) => {
    const method = response.config.method?.toLowerCase();
    if (method === 'post' || method === 'delete' 
      && response.status >= 200 && response.status < 300
    ) {
      const message = response.data.message
      if (message) {
        toast.success(message);
      }
    }
    return response;
  },
  (error) => {
    console.error(error.response?.data?.detail);
    toast.error(`Error sending request: ${error.response?.data?.detail}`);
    return Promise.reject(error);
  }
)

export default api;