import subprocess

from db.database_dump import DatabaseDump


class PostgresDump(DatabaseDump):
    def dump(self, output: str) -> str:
        command = f"PGPASSWORD='{self.password}' pg_dump --inserts -h {self.host} -p {self.port} -U {self.user} {self.db_name} > {output}.sql"
        subprocess.run(command, shell=True, check=True)
        return f"{output}.sql"

