from enum import Enum
from typing import List, Pattern, Sequence


ReplacementRule = List[tuple[Pattern, str]]
Path_Data = Sequence[tuple[str, str]]


class TextCleanerPro(Enum):
    TREE = "tree_replacements"
    COMMENT = "comment_replacements"


class RunMode(Enum):
    NORMAL = "normal"
    DRY_RUN = "dry-run"
    VERBOSE = "verbose"
