from Type import Path_Data
from utils.validation import Validation


class PathBuilder:
    def __init__(self, validation: Validation, indent: int =4) -> None:
        self.__validation = validation
        self._template_paths: Path_Data = []
        self._indent = indent

    def find_indent_level(self, line: str):
        indent = len(line) - len(line.lstrip(" "))
        level = indent // self._indent
        return level

    def build_path(self, template_file: Path_Data):
        if not template_file:
            return
        _template_stack: list[str] = []
        _remove_duplicate: set[tuple[str, str]] = set()

        for line in template_file:
            level = self.find_indent_level(line[0])
            _template_stack = _template_stack[:level] + [line[0].strip()]
            path = "".join(_template_stack)
            if self.__validation.invalid_line(path):
                continue
            _remove_duplicate.add((path, line[1]))
        self._template_paths = sorted(list(_remove_duplicate))
