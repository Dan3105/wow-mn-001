import api from '@/services/api';

export const getFiles = async (src: string = "") => {
    const response = await api.get(`/rag/directories/${src}`);
    return response.data;
};

export const uploadFile = async (path: string, file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('parent_path', path);
    
    const response = await api.post('/rag/directories/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};