import subprocess

from db.database_dump import DatabaseDump


class PostgresDump(DatabaseDump):
    def dump(self, output_file: str):
        command = f"PGPASSWORD='{self.password}' pg_dump --inserts -h {self.host} -p {self.port} -U {self.user} {self.db_name} > {output_file}"
        subprocess.run(command, shell=True, check=True)

