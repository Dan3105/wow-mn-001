import React, { useState, useCallback, useEffect } from "react"
import { useDropzone } from "react-dropzone"
import { ResourceMeta } from "./types/file_type"
import FilesTable from "./components/files_table"
import { createDirectory, getFiles, uploadFile } from "./api"
import { Upload, ChevronLeft, FolderPlus } from "lucide-react"
import { Button } from "@/components/ui/button"
import DirectoryModal from "./components/directory_modal"

const FilesManagementPage: React.FC = () => {
    const [resources, setResources] = useState<ResourceMeta | null>(null);
    const [currentPath, setCurrentPath] = useState("");
    const [isDirectoryModalOpen, setIsDirectoryModalOpen] = useState(false);

    const refreshDirectories = async (path: string) => {
        const fetchedResources = await getFiles(path);
        setResources(fetchedResources);
    };

    useEffect(() => {
        refreshDirectories(currentPath);
    }, [currentPath]);

    const onDrop = useCallback(async (acceptedFiles: File[]) => {
        try {
            await Promise.all(
                acceptedFiles.map(file => uploadFile(currentPath, file))
            );
            refreshDirectories(currentPath);
        } catch (error) {
            console.error("Error uploading files:", error);
        }
    }, [currentPath]);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

    const handleDirectoryClick = (path: string) => {
        setCurrentPath(path);
    };

    const goToRoot = () => {
        refreshDirectories("");
    };

    const handleAddDirectory = async (folderName: string) => {
        try {
            const response = await createDirectory(currentPath, folderName);
            if (response.status === 200) {
                await refreshDirectories(currentPath);
                setIsDirectoryModalOpen(false);
            }
        } catch (error) {
            console.error("Error creating directory:", error);
        }
    };
    
    return (
        <div className="container mx-auto p-4 space-y-4">
            <div className="flex flex-wrap gap-4 items-center">
                <Button 
                    variant="outline" 
                    onClick={goToRoot}
                    className="flex items-center gap-2"
                >
                    <ChevronLeft className="h-4 w-4" />
                    Root Directory
                </Button>
                <Button 
                    variant="outline" 
                    onClick={() => setIsDirectoryModalOpen(true)}
                    className="flex items-center gap-2"
                >
                    <FolderPlus className="h-4 w-4" />
                    New Folder
                </Button>   
                <div
                    {...getRootProps()}
                    className={`flex-grow border-2 border-dashed rounded-lg p-4 cursor-pointer transition-colors ${
                        isDragActive ? "border-primary bg-primary/25" : "border-muted-foreground/50 hover:border-primary/50"
                    }`}
                >
                    <input {...getInputProps()} />
                    <div className="flex items-center justify-center gap-2">
                        <Upload className="h-4 w-4" />
                        <span>{isDragActive ? "Drop files here" : "Drop files or click to upload"}</span>
                    </div>
                </div>
            </div>

            {resources ? (
                <FilesTable 
                    resourceMeta={resources}
                    onDirectoryClick={handleDirectoryClick}
                    refresh={refreshDirectories}
                />
                ) : (
                <div className="text-center py-8 text-gray-500">
                    No resources found at this location
                </div>
            )}
                
                {isDirectoryModalOpen && (
                <DirectoryModal
                    isOpen={isDirectoryModalOpen}
                    onClose={() => setIsDirectoryModalOpen(false)}
                    onSubmit={handleAddDirectory}
                    current_path={currentPath}
                />
            )}
        </div>
    )
}

export default FilesManagementPage
