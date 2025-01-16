import React from "react"
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Download, Eye, Folder, MoreVertical, Pencil, Trash2 } from "lucide-react"
import { FileMeta, DirectoryMeta } from "../types/file_type"

interface FilesTableProps {
    files: FileMeta[]
    directories: DirectoryMeta[]
    onDirectoryClick: (directory: DirectoryMeta) => void
    onDelete: (file: FileMeta) => void
}

const FilesTable: React.FC<FilesTableProps> = ({ 
    files, 
    directories, 
    onDirectoryClick, 
    onDelete 
}) => {
    const formatFileSize = (bytes: number): string => {
        if (bytes === 0) return "0 Bytes"
        const k = 1024
        const sizes = ["Bytes", "KB", "MB", "GB"]
        const i = Math.floor(Math.log(bytes) / Math.log(k))
        return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`
    }

    const formatDate = (dateString: string) => {
        return new Date(dateString).toLocaleString()
    }

    return (
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
                    {/* Directories */}
                    {directories.map((directory) => (
                        <TableRow 
                            key={directory.path}
                            className="cursor-pointer hover:bg-muted"
                            onClick={() => onDirectoryClick(directory)}
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
                            <TableCell className="text-right">
                                <Button variant="ghost" size="icon">
                                    <MoreVertical className="h-4 w-4" />
                                </Button>
                            </TableCell>
                        </TableRow>
                    ))}

                    {/* Files */}
                    {files.map((file) => (
                        <TableRow key={file.path}>
                            <TableCell className="font-medium">{file.name}</TableCell>
                            <TableCell>{formatFileSize(file.size)}</TableCell>
                            <TableCell>{formatDate(file.create_date)}</TableCell>
                            <TableCell>{formatDate(file.modified_date)}</TableCell>
                            <TableCell className="text-right">
                                <DropdownMenu>
                                    <DropdownMenuTrigger asChild>
                                        <Button variant="ghost" size="icon">
                                            <MoreVertical className="h-4 w-4" />
                                        </Button>
                                    </DropdownMenuTrigger>
                                    <DropdownMenuContent align="end">
                                        <DropdownMenuItem>
                                            <Eye className="mr-2 h-4 w-4" />
                                            Preview
                                        </DropdownMenuItem>
                                        <DropdownMenuItem>
                                            <Download className="mr-2 h-4 w-4" />
                                            Download
                                        </DropdownMenuItem>
                                        <DropdownMenuItem>
                                            <Pencil className="mr-2 h-4 w-4" />
                                            Rename
                                        </DropdownMenuItem>
                                        <DropdownMenuItem
                                            className="text-destructive"
                                            onClick={() => onDelete(file)}
                                        >
                                            <Trash2 className="mr-2 h-4 w-4" />
                                            Delete
                                        </DropdownMenuItem>
                                    </DropdownMenuContent>
                                </DropdownMenu>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </div>
    )
}

export default FilesTable