import os
from config.ConfigManager import Config


class Validation:
    def __init__(self, config: Config) -> None:
        self.config = config

    def validate_file(self):
        if not os.path.exists(self.config.file_path):
            return False
        return True

    def validate_folder(self):
        if not os.path.exists(self.config.output_dir):
            return False
        return True

    def permission_check(self):
        if not os.access(self.config.output_dir, os.W_OK):
            return False
        return True

    @staticmethod
    def validate_file_extension(line: str):
        if not line.endswith("/"):
            file_name = line.strip()
            if "." in file_name:
                ext = file_name.split(".")[-1]
                if len(ext) > 20:
                    return False
                return True
        return False

    def invalid_line(self, line: str):
        normalize_line = os.path.normpath(line)
        basename = os.path.basename(normalize_line)

        invalid_name = self.config.invalid_filenames
        if basename.lower() in invalid_name:
            return True
        return False
