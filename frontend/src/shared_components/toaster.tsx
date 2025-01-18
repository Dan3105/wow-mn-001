import { Toaster } from "react-hot-toast";

export function ToastProvider() {
    return (
        <>
            <Toaster 
                position="top-right" 
                gutter={8} 
                containerStyle={{
                    zIndex: 9999,
                }}
                toastOptions={{
                    duration: 3000,
                    style: {
                        padding: '16px',
                        maxWidth: '500px',
                        wordBreak: 'break-word'
                    },
                }}
            />
        </>
    );
}