from fastapi import FastAPI
from configuration import router_config
import argparse

app = FastAPI()
app.include_router(router=router_config.router)

def main():
    import uvicorn

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run the FastAPI application.")
    parser.add_argument(
        "--reload", 
        action="store_true",  # This makes it a flag (default is False)
        help="Enable or disable auto-reload (default: False)"
    )
    parser.add_argument(
        "--host", 
        type=str, 
        default="0.0.0.0", 
        help="Host for the application (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8080, 
        help="Port for the application (default: 8080)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Use the import string "module_name:app" for reload compatibility
    uvicorn.run(
        app="app:app",  # Replace 'main' with your actual module name
        host=args.host,
        port=args.port,
        reload=args.reload
    )

if __name__ == '__main__':
    main()
