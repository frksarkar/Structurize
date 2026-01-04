from typing import Tuple
from tqdm import tqdm
from pathlib import Path
from utils.validation import Validation
from Type import Path_Data


class FolderGenerator:

    def __init__(self, validation: Validation, save_folder: Path):
        self.__validation = validation
        self.__save_folder: Path = save_folder

    def generate_folder(self, template_paths: Path_Data):
        if not template_paths:
            return

        project_name = template_paths[0][0].replace("/", "")

        for path in tqdm(template_paths, desc=project_name):
            self._generate_file_or_folder(path)

    def _generate_file_or_folder(self, path: Tuple[str, str]):
        # full path
        file_path = self.__save_folder / path[0]

        # separate doc
        doc = self._format_command(path[1], file_path.suffix)

        # make file or folder
        if not self.__validation.validate_file_extension(path[0]):
            file_path.mkdir(parents=True, exist_ok=True)
            if path[1]:
                doc_file = file_path / "README.md"
                doc_file.write_text(doc or "", encoding="utf-8")
        else:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(doc or "", encoding="utf-8")

    def _format_command(self, doc: str, ext: str):
        if not doc:
            return
        ext = ext.lower()
        if ext in ("py", "pyw"):
            return f"# {doc} \n"
        elif ext in ("md", "txt"):
            return f"## {doc} \n"
        elif ext in ("json"):
            return f"## {doc} \n"
        elif ext in ("html", "css", "js"):
            return f"// {doc} \n"
        elif ext in ("html", "xml"):
            return f"<!-- {doc} --> \n"
        else:
            return f"# {doc} \n"
