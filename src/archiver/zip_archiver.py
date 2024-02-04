import os
import zipfile

from archiver.base_archiver import BaseArchiver


class CustomZipArchiver(BaseArchiver):
    def get_output_filename(self):
        return f"{self._output_filename}.zip"

    def create_archive(self):
        """Creating an archive with ZipFile lib"""
        with zipfile.ZipFile(f"{self._output_filename}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for path in self._paths:
                if not path:
                    continue
                if os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            file_path = str(os.path.join(root, file))
                            arc_name = os.path.relpath(file_path, start=os.path.commonpath([path]))
                            zipf.write(file_path, arc_name)
                else:
                    zipf.write(path, arcname=os.path.basename(path))
