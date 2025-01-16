import React, { useState, useCallback, useEffect } from "react"
import { useDropzone } from "react-dropzone"
import { ResourceMeta, DirectoryMeta } from "./types/file_type"
import FilesTable from "./components/files_table"
import { getFiles, uploadFile } from "./api"
import { Upload, ChevronLeft } from "lucide-react"
import { Button } from "@/components/ui/button"

const FilesManagementPage: React.FC = () => {
    const [resources, setResources] = useState<ResourceMeta | null>(null)
    const [currentPath, setCurrentPath] = useState("")

    useEffect(() => {
        const fetchResources = async () => {
            const fetchedResources = await getFiles(currentPath)
            setResources(fetchedResources)
        }
        fetchResources()
    }, [currentPath])

    const onDrop = useCallback(async (acceptedFiles: File[]) => {
        try {
            await Promise.all(
                acceptedFiles.map(async (file) => {
                    await uploadFile(currentPath, file)
                })
            )
            const updatedResources = await getFiles(currentPath)
            setResources(updatedResources)
        } catch (error) {
            console.error("Error uploading files:", error)
        }
    }, [currentPath])

    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop })

    const handleDirectoryClick = (directory: DirectoryMeta) => {
        setCurrentPath(directory.path)
    }

    const handleGoBack = () => {
        if (resources?.parent_path) {
            setCurrentPath(resources.parent_path)
        }
    }

    return (
        <div className="container mx-auto p-4 space-y-4">
            <div className="flex justify-between items-center">
                {resources?.parent_path && (
                    <Button 
                        variant="outline" 
                        onClick={handleGoBack}
                        className="flex items-center gap-2"
                    >
                        <ChevronLeft className="h-4 w-4" />
                        Back
                    </Button>
                )}
                <div
                    {...getRootProps()}
                    className={`border-2 border-dashed rounded-lg p-4 cursor-pointer ${
                        isDragActive ? "border-primary" : "border-muted"
                    }`}
                >
                    <input {...getInputProps()} />
                    <div className="flex items-center gap-2">
                        <Upload className="h-4 w-4" />
                        <span>{isDragActive ? "Drop files here" : "Upload files"}</span>
                    </div>
                </div>
            </div>

            <FilesTable 
                files={resources?.files || []}
                directories={resources?.directories || []}
                onDirectoryClick={handleDirectoryClick}
                onDelete={() => {}}
            />
        </div>
    )
}

export default FilesManagementPage
