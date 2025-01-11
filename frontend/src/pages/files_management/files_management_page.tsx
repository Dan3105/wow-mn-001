import React, { useState, useCallback } from "react"
import { useDropzone } from "react-dropzone"
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
    Download,
    Eye,
    MoreVertical,
    Pencil,
    Search,
    Trash2,
    Upload,
} from "lucide-react"
import SimpleModal from "@/shared_components/modals/simple_modal"

// Types
interface FileItem {
    id: string
    name: string
    type: string
    size: number
    uploadDate: Date
    url: string
}

interface SortConfig {
    key: keyof FileItem
    direction: "asc" | "desc"
}

const FilesManagementPage: React.FC = () => {
    const [files, setFiles] = useState<FileItem[]>([])
    const [searchQuery, setSearchQuery] = useState("")
    const [sortConfig] = useState<SortConfig>({
        key: "uploadDate",
        direction: "desc",
    })
    const [selectedFile, setSelectedFile] = useState<FileItem | null>(null)
    const [isDeleteDialogOpen, setIsDeleteDialogOpen] = useState(false)

    // File upload handling
    const onDrop = useCallback((acceptedFiles: File[]) => {
        const newFiles: FileItem[] = acceptedFiles.map((file) => ({
            id: crypto.randomUUID(),
            name: file.name,
            type: file.type,
            size: file.size,
            uploadDate: new Date(),
            url: URL.createObjectURL(file),
        }))
        setFiles((prev) => [...prev, ...newFiles])
    }, [])

    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop })

    // Sort and filter functions
    const sortFiles = (files: FileItem[]): FileItem[] => {
        return [...files].sort((a, b) => {
            const aValue = a[sortConfig.key]
            const bValue = b[sortConfig.key]
            if (sortConfig.direction === "asc") {
                return aValue < bValue ? -1 : 1
            }
            return aValue > bValue ? -1 : 1
        })
    }

    const filteredFiles = sortFiles(
        files.filter((file) =>
            file.name.toLowerCase().includes(searchQuery.toLowerCase())
        )
    )

    // File actions
    const handleDelete = (file: FileItem) => {
        setFiles((prev) => prev.filter((f) => f.id !== file.id))
        setIsDeleteDialogOpen(false)
    }

    const formatFileSize = (bytes: number): string => {
        if (bytes === 0) return "0 Bytes"
        const k = 1024
        const sizes = ["Bytes", "KB", "MB", "GB"]
        const i = Math.floor(Math.log(bytes) / Math.log(k))
        return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`
    }

    return (
        <div className="container mx-auto p-4 space-y-4">
            {/* Header with search and upload */}
            <div className="flex justify-between items-center gap-4">
                <div className="relative flex-1 max-w-sm">
                    <Search className="absolute left-2 top-2.5 mr-16 h-4 w-4 text-muted-foreground" />
                    <Input
                        placeholder="Search files..."
                        className="pl-8"
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                    />
                </div>
                <div
                    {...getRootProps()}
                    className={`border-2 border-dashed rounded-lg p-4 cursor-pointer ${
                        isDragActive ? "border-primary" : "border-muted"
                    }`}
                >
                    <input {...getInputProps()} />
                    <div className="flex items-center gap-2" color="to-slate-500">
                        <Upload className="h-4 w-4" />
                        <span>{isDragActive ? "Drop files here" : "Upload files"}</span>
                    </div>
                </div>
            </div>

            {/* File list */}
            <div className="border rounded-lg">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Name</TableHead>
                            <TableHead>Type</TableHead>
                            <TableHead>Size</TableHead>
                            <TableHead>Upload Date</TableHead>
                            <TableHead className="text-right">Actions</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {filteredFiles.map((file) => (
                            <TableRow key={file.id}>
                                <TableCell>{file.name}</TableCell>
                                <TableCell>{file.type}</TableCell>
                                <TableCell>{formatFileSize(file.size)}</TableCell>
                                <TableCell>
                                    {file.uploadDate.toLocaleDateString()}
                                </TableCell>
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
                                                onClick={() => {
                                                    setSelectedFile(file)
                                                    setIsDeleteDialogOpen(true)
                                                }}
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

            {/* Delete confirmation dialog */}
            <SimpleModal
                isOpen={isDeleteDialogOpen}
                onClose={() => setIsDeleteDialogOpen(false)}
                onConfirm={() => selectedFile && handleDelete(selectedFile)}
                title="Delete File"
                description={`Are you sure you want to delete "${selectedFile?.name}"?. This action cannot be undone.`}
                confirmButtonText="Delete"
            />
        </div>
    )
}

export default FilesManagementPage