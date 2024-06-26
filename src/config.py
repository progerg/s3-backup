from os import getenv


ENDPOINT_URL = getenv("ENDPOINT_URL")
BUCKET = getenv("BUCKET")
SERVICE_NAME = getenv("SERVICE_NAME", "s3")

DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")
DB_LOGIN = getenv("DB_LOGIN")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_COLLECTION = getenv("DB_COLLECTION")
DB_TYPE = getenv("DB_TYPE", "postgres")

FILES = getenv("FILES", "")

BACKUP_INTERVAL = int(getenv("BACKUP_INTERVAL", 0))
SPECIFIC_TIME = getenv("SPECIFIC_TIME", "")

AWS_SECRET_KEY = getenv("AWS_SECRET_KEY")
AWS_ACCESS_KEY = getenv("AWS_ACCESS_KEY")

TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")
TG_CHAT_ID = getenv("TG_CHAT_ID")

BACKUP_NAME_FOR_TG = getenv("BACKUP_NAME_FOR_TG", "Backup")
