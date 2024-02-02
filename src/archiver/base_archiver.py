class BaseArchiver:
    def __init__(self, paths: list[str], output_filename: str):
        self._paths = paths
        self._output_filename = output_filename

    def get_output_filename(self):
        return self._output_filename

    def get_paths(self) -> list[str]:
        return self._paths.copy()

    def add_file(self, path: str):
        self._paths.append(path)

    def create_archive(self):
        raise NotImplementedError("create_archive must be implemented by subclasses.")
