import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Download, Eye, MoreVertical, Pencil, Trash2 } from "lucide-react"

interface ActionsDropdownProps {
    onDelete: () => void
    className?: string
}

export const ActionsDropdown: React.FC<ActionsDropdownProps> = ({ onDelete, className }) => (
    <DropdownMenu>
        <DropdownMenuTrigger asChild onClick={e => e.stopPropagation()}>
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
                className={`text-destructive ${className}`}
                onClick={(e) => {
                    e.stopPropagation()
                    onDelete()
                }}
            >
                <Trash2 className="mr-2 h-4 w-4" />
                Delete
            </DropdownMenuItem>
        </DropdownMenuContent>
    </DropdownMenu>
)
