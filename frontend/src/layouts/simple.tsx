import React from 'react';
import { Link } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { cn } from "@/lib/utils";

const SimpleLayout: React.FC = () => {
    return (
        <div className="min-h-screen">
            <nav className="border-b bg-background">
                <div className="flex h-14 items-center px-4">
                    <Link 
                        to="/" 
                        className={cn(
                            "text-sm font-medium transition-colors hover:text-primary",
                        )}
                    >
                        Home
                    </Link>
                </div>
            </nav>
            <main className="flex-1 p-4">
                <Outlet />
            </main>
        </div>
    );
};



export default SimpleLayout;