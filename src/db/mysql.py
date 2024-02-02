import subprocess

from db.database_dump import DatabaseDump


class MySQLDump(DatabaseDump):
    def dump(self, output: str):
        command = f"mysqldump -h {self.host} -P {self.port} -u {self.user} -p '{self.password}' {self.db_name} > {output}.sql"
        subprocess.run(command, shell=True, check=True)

