from pathlib import Path
from typing import List


class FileManage:
    def __init__(self, file_name: Path) -> None:
        self._template_file: List[str] = []
        self.__structure_file_path: Path = file_name

    def read_structure_file(self) -> list[str]:
        if not Path.exists(self.__structure_file_path):
            return []
        try:
            with open(self.__structure_file_path, "r", encoding="utf-8") as f:
                self._template_file = [line for line in f]
        except OSError:
            return []
        return self._template_file
