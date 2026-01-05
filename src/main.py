import os

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.ConfigManager import Config
from utils.validation import Validation
from utils.file_io import FileManage
from core.template_parser import TemplateProcessor
from utils.path_builder import PathBuilder
from core.folder_builder import FolderGenerator
from utils.text_cleaner import TextCleaner


class Main:
    def __init__(self):
        self.d_config = Config()
        self.v_field = Validation(self.d_config)

    def run_files(self):
        files = os.listdir(self.d_config.working_dir)
        tree_files = [file for file in files if file.endswith(".tree")]

        if not tree_files:
            return

        if self.d_config.multi_file_mode:
            for file in tree_files:
                if file.endswith(".tree"):
                    self.d_config.file_path = file
                    self.render_file()
                    print(end="\n")
        else:
            self.d_config.file_path = tree_files[0]
            self.render_file()
            print(end="\n")

    def render_file(self):
        fm = FileManage(self.d_config.file_path)
        fm.read_structure_file()
        tp = TemplateProcessor(TextCleaner())
        tp.extract_name_and_doc(fm.template_file)
        tp.clean_template_file()
        tp.strip_tree_symbols()
        fs = PathBuilder(self.v_field, self.d_config.indent)
        fs.build_path(tp.clean_path)
        gf = FolderGenerator(self.v_field, self.d_config.output_dir)
        gf.generate_folder(fs.template_paths)


if __name__ == "__main__":
    Main().run_files()
    print("✅ Project structure generated successfully!", end="\n")
