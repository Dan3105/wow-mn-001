import api from '@/services/api';
import { ResourceMeta } from '../types/file_type';

export const getFiles = async (src: string = ""): Promise<ResourceMeta> => {
    const response = await api.get(`/rag/directories/${src}`);
    return response.data;
};

export const uploadFile = async (path: string, file: File) => {
    const formData = new FormData();
    formData.append('parent_path', path);
    formData.append('file', file);
    
    const response = await api.post('/rag/directories/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const uploadFiles = async (path: string, files: File[]) => {
    const formData = new FormData();
    formData.append('parent_path', path);
    files.forEach(file => {
        formData.append('files', file);
    });
    
    const response = await api.post('/rag/directories/upload-files', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const createDirectory = async (folder: string, name: string) => {
    const formData = new FormData();
    formData.append('folder', folder);
    formData.append('name', name);
    
    const response = await api.post('/rag/directories/create-directory', formData);
    return response;
};

export const deleteFile = async (fileName: string, currentPath: string) => {
    const formData = new FormData();
    formData.append('file_name', fileName);
    formData.append('curr_path', currentPath);
    
    const response = await api.delete('/rag/directories/delete-file', {
        data: formData
    });
    return response.data;
};

export const deleteDirectory = async (currentPath: string) => {
    const formData = new FormData();
    formData.append('curr_path', currentPath);
    
    const response = await api.delete('/rag/directories/delete-directory', {
        data: formData
    });
    return response.data;
};

export const renameResource = async (fileName: string, newName: string, currentPath: string) => {
    const formData = new FormData();
    formData.append('file_name', fileName);
    formData.append('dst', newName);
    formData.append('curr_path', currentPath);
    
    const response = await api.post('/rag/directories/rename', formData);
    return response.data;
};

export const moveResource = async (sourcePath: string, destinationPath: string) => {
    const formData = new FormData();
    formData.append('src', sourcePath);
    formData.append('dst', destinationPath);
    
    const response = await api.post('/rag/directories/move', formData);
    return response.data;
};