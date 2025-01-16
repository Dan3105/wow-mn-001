export interface FileMeta {
    name: string;
    path: string;
    hash: string;
    size: number;
    create_date: string; 
    modified_date: string;
}

export interface DirectoryMeta {
    name: string;
    path: string;
    create_date: string;
    modified_date: string;
}

export interface ResourceMeta {
    parent_path: string;
    path: string;
    directories: DirectoryMeta[];
    files: FileMeta[];
}