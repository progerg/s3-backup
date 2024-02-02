import datetime
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
    def remove_files(files: list[str]):
        for path in files:
            if path and os.path.isfile(path):
                os.remove(path)

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
            self.db_dump.dump(database_dump_file)
            self.archiver.add_file(database_dump_file)

        self.archiver.create_archive()

        return self.archiver.get_output_filename(), database_dump_file

