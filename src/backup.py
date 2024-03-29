import datetime
import logging
import os
import shutil

from db.database_dump import DatabaseDump
from archiver.base_archiver import BaseArchiver


class NoArchiver(Exception):
    pass


class Backup:
    def __init__(self, archiver: BaseArchiver, db_dump: DatabaseDump = None):
        self.db_dump = db_dump
        self.archiver = archiver

    @staticmethod
    def remove_paths(files: list[str]):
        for path in files:
            if path and os.path.isfile(path):
                logging.info(f"Removing file {path}")
                os.remove(path)
            elif path and os.path.isdir(path):
                logging.info(f"Removing folder {path}")
                shutil.rmtree(path)

    def perform_backup(self):
        """
        Performing the backup process

        :return:
        """
        if not self.archiver:
            raise NoArchiver("No archiver provided for archiving the files")

        database_dump_file = None
        if self.db_dump:
            database_dump_file = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
            database_dump_file = self.db_dump.dump(database_dump_file)
            self.archiver.add_file(database_dump_file)

        self.archiver.create_archive()

        return self.archiver.get_output_filename(), database_dump_file

