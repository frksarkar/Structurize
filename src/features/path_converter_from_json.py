import os
import sys
import json
from Type import Path_Data
from typing import List, Union

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


JsonFileType = dict[str, Union[str, 'JsonFileType', List[Union[str, 'JsonFileType']]]]

class JsonToStructure:
   
    def __init__(self):
        self.path: Path_Data = []
        self.__json_file: JsonFileType = {}
    
    def load_json(self, path_data: List[str]):
        jsonFile = ''
        for line in path_data:
            jsonFile += line
        self.__json_file = json.loads(jsonFile)
        
    def make_path_to_dict(self):
        self.__loop_stack(self.__json_file)
    
    def __loop_stack(self, stack: JsonFileType, level: list[str]=[]):
        
        for key, value in stack.items():            
            if isinstance(value, dict) and len(value) > 0:
                level.append(key)
                self.__loop_stack(value, level)
                level.pop()

            elif  isinstance(value, list):
                
                for item in value:
                    if isinstance(item, dict) and len(item) > 0:
                        level.append(key)
                        self.__loop_stack(item, level)
                        level.pop()
                    else:
                        if isinstance(item, str):
                            level.append(item)
                        path = '/'.join(level)
                        self.path.append((path, ''))
                        level.pop()
                    
            else:
                level.append(key)
                path = '/'.join(level)
                if isinstance(value, str):
                    self.path.append((path, value))
                level.pop()


