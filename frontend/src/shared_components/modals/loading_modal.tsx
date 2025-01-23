import { Loader2 } from "lucide-react"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog"

interface LoadingModalProps {
    isOpen: boolean
    title?: string
    description?: string
}

export function LoadingModal({
    isOpen,
    title = "Please wait",
    description = "This may take a few moments...",
}: LoadingModalProps) {
    return (
        <Dialog open={isOpen} onOpenChange={() => {}}>
            <DialogContent className="sm:max-w-[425px]">
                <DialogHeader>
                    <DialogTitle>{title}</DialogTitle>
                    <DialogDescription>{description}</DialogDescription>
                </DialogHeader>
                <div className="flex items-center justify-center py-6">
                    <Loader2 className="h-8 w-8 animate-spin" />
                </div>
            </DialogContent>
        </Dialog>
    )
}