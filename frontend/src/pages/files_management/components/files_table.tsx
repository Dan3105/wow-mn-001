import React, { useState } from "react"
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"

import { Folder, RotateCw} from "lucide-react"
import { FileMeta, DirectoryMeta, ResourceMeta } from "../types/file_type"
import SimpleModal from "@/shared_components/modals/simple_modal"
import { deleteDirectory, deleteFile, moveResource } from "../api"
import { ActionsDropdown } from "./actions_dropdown"
import { formatDate, formatFileSize } from "../files_management_func"
import { Button } from "@/components/ui/button"

interface FilesTableProps {
    resourceMeta: ResourceMeta
    onDirectoryClick: (path: string) => void
    refresh: (path: string) => void
}

const FilesTable: React.FC<FilesTableProps> = ({
    resourceMeta, 
    onDirectoryClick,
    refresh
    }) => {
    const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false)
    const [functionHandler, setFunctionHandler] = useState<(() => Promise<void>)>()
    const [selectResourceItem, setSelectResourceItem] = useState<FileMeta | DirectoryMeta | null>(null)
    const [targetResourceItem, setTargetResourceItem] = useState<string>("")

    const handleDeleteFile = (file: FileMeta) => {
        setIsDeleteModalOpen(true)
        setFunctionHandler(() => async () => {
            await deleteFile(file.path, resourceMeta.path)
            refresh(resourceMeta.path)
        })
    }
    
    const handleDeleteDirectory = (folder: DirectoryMeta) => {
        setIsDeleteModalOpen(true)
        setFunctionHandler(() => async () => {
            await deleteDirectory(folder.path)
            refresh(resourceMeta.path)
        })
    }

    const handleDirectoryClick = (e: React.MouseEvent, path: string) => {
        const target = e.target as HTMLElement
        if (!target.closest('.actions-cell')) {
            onDirectoryClick(path)
        }
    }

    const handleMoveFile = async () => {
        // console.log(`Move file from: ${selectResourceItem?.path} to: ${targetResourceItem}`)
        if (selectResourceItem && targetResourceItem
        ) {
            if (selectResourceItem as FileMeta) {
                const file = selectResourceItem as FileMeta
                // Move file
                if (resourceMeta.path === targetResourceItem) {
                    return;
                }
                await moveResource(file.path, targetResourceItem)   
            }
            else if (selectResourceItem as DirectoryMeta) {
                const directory = selectResourceItem as DirectoryMeta
                // Move directory
                await moveResource(directory.path, targetResourceItem)
            }
            
            refresh(resourceMeta.path)
        }
    }

    return (
        <>
            <div className="flex justify-between items-center mb-4">
                <div className="text-sm text-muted-foreground flex items-center gap-2">
                    <span className="font-medium">Current Directory:</span>
                    <span>{resourceMeta.path || "Root"}</span>
                </div>
                <Button
                    variant="outline"
                    size="sm"
                    onClick={() => refresh(resourceMeta.path)}
                    className="flex items-center gap-2"
                >
                    <RotateCw className="h-4 w-4" />
                    Refresh
                </Button>
            </div>
            <div className="border rounded-lg">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Name</TableHead>
                            <TableHead>Size</TableHead>
                            <TableHead>Created Date</TableHead>
                            <TableHead>Modified Date</TableHead>
                            <TableHead className="text-right">Actions</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {resourceMeta.parent_path && (
                            <TableRow
                                key={resourceMeta.parent_path}
                                className="cursor-pointer hover:bg-muted"
                                onClick={() => onDirectoryClick(resourceMeta.parent_path)}
                                onDragOver={() => {setTargetResourceItem(resourceMeta.parent_path)}}
                                onDragLeave={() => {setTargetResourceItem("")}}
                                onDrop={() => {handleMoveFile()}}
                            >
                                <TableCell className="font-medium">
                                    <div className="flex items-center gap-2">
                                        <Folder className="h-4 w-4" />
                                        ..
                                    </div>
                                </TableCell>
                                <TableCell>--</TableCell>
                                <TableCell>--</TableCell>
                                <TableCell>--</TableCell>
                                <TableCell>--</TableCell>
                            </TableRow>
                        )}
                        {resourceMeta.directories.map((directory) => (
                            <TableRow 
                                draggable
                                key={directory.path}
                                className="cursor-pointer hover:bg-muted"
                                onClick={(e) => handleDirectoryClick(e, directory.path)}
                                onDragStart={() => {setSelectResourceItem(directory)}}
                                onDragEnd={() => {setSelectResourceItem(null)}}
                                onDragLeave={() => {setTargetResourceItem("")}}
                                onDragOver={() => {setTargetResourceItem(directory.path)}}
                                onDrop={() => {handleMoveFile()}}
                            >
                                <TableCell className="font-medium">
                                    <div className="flex items-center gap-2">
                                        <Folder className="h-4 w-4" />
                                        {directory.name}
                                    </div>
                                </TableCell>
                                <TableCell>--</TableCell>
                                <TableCell>{formatDate(directory.create_date)}</TableCell>
                                <TableCell>{formatDate(directory.modified_date)}</TableCell>
                                <TableCell className="text-right actions-cell">
                                    <ActionsDropdown onDelete={() => handleDeleteDirectory(directory)} />
                                </TableCell>
                            </TableRow>
                        ))}
                        {resourceMeta.files.map((file) => (
                            <TableRow key={file.path}
                                draggable
                                onDragStart={() => {setSelectResourceItem(file)}}
                                onDragEnd={() => {setSelectResourceItem(null)}}
                            >
                                <TableCell className="font-medium">{file.name}</TableCell>
                                <TableCell>{formatFileSize(file.size)}</TableCell>
                                <TableCell>{formatDate(file.create_date)}</TableCell>
                                <TableCell>{formatDate(file.modified_date)}</TableCell>
                                <TableCell className="text-right">
                                    <ActionsDropdown onDelete={() => handleDeleteFile(file)} />
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </div>
            
            {isDeleteModalOpen && (
                <SimpleModal 
                    isOpen={isDeleteModalOpen}
                    onClose={() => setIsDeleteModalOpen(false)}
                    onConfirm={async () => {
                        if (functionHandler) {
                            await functionHandler();
                            setIsDeleteModalOpen(false);
                            onDirectoryClick(resourceMeta.parent_path);
                        }
                    }}
                    title="Delete File"
                    description="Are you sure you want to delete this file?"
                />
            )}
        </>
    )
}

export default FilesTable
