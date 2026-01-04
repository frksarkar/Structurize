from Type import Path_Data
from config.config import Config
from utils.text_cleaner import TextCleaner, TextCleanerPro


class TemplateProcessor:

    def __init__(self, config: TextCleaner) -> None:
        self.config = config
        self.clean_path: Path_Data = []
        self.d_config = Config()

    def strip_tree_symbols(self):
        if not self.clean_path:
            return
        clean_path = []
        for line in self.clean_path:
            name = self.config.clean_text(TextCleanerPro.TREE, line[0])
            if name.isspace():
                continue
            clean_path.append((name, line[1]))
        self.clean_path = clean_path

    def clean_template_file(self):
        if not self.clean_path:
            return
        clean_path = []

        for line in self.clean_path:
            name = self.config.clean_text(TextCleanerPro.COMMENT, line[0])
            clean_path.append((name, line[1]))
        self.clean_path = clean_path

    def extract_name_and_doc(self, template_file: list[str]):
        speared_name_and_doc = []
        separator = self.d_config.doc_separator
        for line in template_file:
            if separator in line:
                path_part, doc_part = line.split(separator, 1)
                speared_name_and_doc.append((path_part, doc_part))
            else:
                speared_name_and_doc.append((line, ""))
        self.clean_path = speared_name_and_doc

    def retrieve_path_doc(self):
        pass
