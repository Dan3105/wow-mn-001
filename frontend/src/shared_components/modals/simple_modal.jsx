import React from "react"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"

const SimpleModal = ({
    isOpen,
    onClose,
    onConfirm,
    title,
    description,
    confirmButtonText = "Confirm",
    cancelButtonText = "Cancel",
    confirmButtonVariant = "destructive",
}) => {
    return (
        <Dialog open={isOpen} onOpenChange={onClose}>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>{title}</DialogTitle>
                    <DialogDescription>{description}</DialogDescription>
                </DialogHeader>
                <div className="flex justify-end gap-2">
                    <Button variant="ghost" onClick={onClose}>
                        {cancelButtonText}
                    </Button>
                    <Button variant={confirmButtonVariant} onClick={onConfirm}>
                        {confirmButtonText}
                    </Button>
                </div>
            </DialogContent>
        </Dialog>
    )
}

export default SimpleModal