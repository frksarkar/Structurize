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
from src.features.path_converter_from_json import JsonToStructure


class Main:
    def __init__(self):
        self.d_config = Config()
        self.v_field = Validation(self.d_config)

    def run_files(self):
        
        check_ext = self.d_config.read_file_extension
        files = os.listdir(self.d_config.working_dir)
        tree_files = [file for file in files if file.endswith(check_ext)]
        
        if not tree_files:
            return

        if  len(tree_files) > 0 and not self.d_config.multi_file_mode:
            last_path = os.path.basename(self.d_config.file_path)
            tree_files = [ file for file in tree_files if file == last_path ]
            
        if check_ext == ".json":
            for file in tree_files:
                if file.endswith(".json"):
                    self.d_config.file_path = file
                    self.render_json()
                    print(end="\n")
        elif check_ext == ".tree":
            for file in tree_files:
                if file.endswith(".tree"):
                    self.d_config.file_path = file
                    self.render_file()
                    print(end="\n")


    def run_config(self):
        pass
        


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

    def render_json(self):
        fm = FileManage(self.d_config.file_path)
        fm.read_structure_file()
        js = JsonToStructure()
        js.load_json(fm.template_file)
        js.make_path_to_dict()
        gf = FolderGenerator(self.v_field, self.d_config.output_dir)
        gf.generate_folder(js.path)

if __name__ == "__main__":
    Main().run_files()
    print("✅ Project structure generated successfully!", end="\n")
