import React from "react"
import { Button } from "@/components/ui/button"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

interface DirectoryModalProps {
    isOpen: boolean
    onClose: () => void
    onSubmit: (folderName: string) => void
    current_path: string
}

const DirectoryModal: React.FC<DirectoryModalProps> = ({
    isOpen,
    onClose,
    onSubmit,
    current_path,
}) => {
    const [folderName, setFolderName] = React.useState("")

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        if (folderName.trim()) {
            onSubmit(folderName.trim())
            setFolderName("")
            onClose()
        }
    }

    return (
        <Dialog open={isOpen} onOpenChange={onClose}>
            <DialogContent className="sm:max-w-[475px]">
                <DialogHeader>
                    <DialogTitle>Create New Folder</DialogTitle>
                    {current_path && <DialogDescription>
                        Create a new folder in: {current_path}
                    </DialogDescription>}
                </DialogHeader>
                <form onSubmit={handleSubmit}>
                    <div className="grid gap-2 py-3">
                        <div className="grid grid-cols-4 items-center gap-3">
                            <Label htmlFor="folderName" className="text-right">
                                Folder Name
                            </Label>
                            <Input
                                id="folderName"
                                value={folderName}
                                onChange={(e) => setFolderName(e.target.value)}
                                className="col-span-3"
                                placeholder="Enter folder name"
                                autoFocus
                            />
                        </div>
                    </div>
                    <DialogFooter>
                        <Button type="button" variant="outline" onClick={onClose}>
                            Cancel
                        </Button>
                        <Button type="submit">Create</Button>
                    </DialogFooter>
                </form>
            </DialogContent>
        </Dialog>
    )
}

export default DirectoryModal