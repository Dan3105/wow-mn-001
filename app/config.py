import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SESSION_PERMANENT = True
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    INSTANCE_PATH = "D:/wow/management/document/db_deployment/volumes/sqlite"
    CHROMA_HOST = os.environ["CHROMA_HOST"]
    CHROMA_PORT = os.environ["CHROMA_PORT"]

    UPLOAD_URL = os.environ["UPLOAD_URL"]
    CELERY = {
        "broker_url": os.environ.get("REDIS_URI", False),
        "task_ignore_result": True,
        "broker_connection_retry_on_startup": False,
    }