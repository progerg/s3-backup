from apscheduler.schedulers.background import BackgroundScheduler

import datetime
import logging

from config import *
from backup import Backup

from db.postgres import PostgresDump
from db.mysql import MySQLDump

from archiver.zip_archiver import CustomZipArchiver

from cloud import CloudS3Uploader


def backup():
    db_dump = None
    if DB_HOST and DB_PORT and DB_NAME and DB_LOGIN and DB_PASSWORD and DB_TYPE:
        if DB_TYPE == "postgres":
            db_dump = PostgresDump(DB_HOST, DB_PORT, DB_LOGIN, DB_PASSWORD, DB_NAME)
        elif DB_TYPE == "mysql":
            db_dump = MySQLDump(DB_HOST, DB_PORT, DB_LOGIN, DB_PASSWORD, DB_NAME)
    else:
        logging.warning("No DB credentials provided")

    archive = CustomZipArchiver(FILES.split(","), datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))
    backup_dump = Backup(archive, db_dump)

    zip_file_path, db_dump_path = backup_dump.perform_backup()

    storage = CloudS3Uploader(SERVICE_NAME, BUCKET, AWS_ACCESS_KEY, AWS_SECRET_KEY, ENDPOINT_URL)
    storage.upload_file(zip_file_path)

    backup_dump.remove_files([zip_file_path, db_dump_path])


if __name__ == "__main__":
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(lambda: backup(), 'interval', seconds=BACKUP_INTERVAL)
    scheduler.start()

    import time

    while True:
        time.sleep(10)

    scheduler.shutdown()
