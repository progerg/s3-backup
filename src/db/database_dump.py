class DatabaseDump:
    def __init__(self, host: str, port: str, user: str, password: str, db_name: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name

    def dump(self, output: str) -> str:
        raise NotImplementedError("dump must be implemented in derived class")

