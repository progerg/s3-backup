import subprocess

from db.database_dump import DatabaseDump


class MongoDBDump(DatabaseDump):
    def __init__(self, host: str, port: str, user: str, password: str, db_name: str, db_collection: str = None):
        super().__init__(host, port, user, password, db_name)
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name
        self.db_collection = db_collection

    def dump(self, output: str):
        command = f"mongodump --host={self.host} --port={self.port} --db={self.db_name} --out={output}"
        if self.user and self.password:
            command += f" --username={self.user} --password={self.password} --authenticationDatabase admin"
        if self.db_collection:
            command += f" --collection={self.db_collection}"
        subprocess.run(command, shell=True, check=True)
