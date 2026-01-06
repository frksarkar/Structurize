from enum import Enum
from typing import List, Pattern, MutableSequence, TypeAlias, Union

ReplacementRule = List[tuple[Pattern[str], str]]
Path_Data = MutableSequence[tuple[str, str]]
ConfigType: TypeAlias = dict[str, Union[str, "ConfigType", list[str]]]


class TextCleanerPro(Enum):
    TREE = "tree_replacements"
    COMMENT = "comment_replacements"


class RunMode(Enum):
    NORMAL = "normal"
    DRY_RUN = "dry-run"
    VERBOSE = "verbose"
