import re
from Type import ReplacementRule, TextCleanerPro
from dataclasses import dataclass, field


@dataclass
class TextCleaner:
    # def __post_init__(self):

    # pattern defined
    tree_replacements: ReplacementRule = field(
        default_factory=lambda: [
            (re.compile(r"├─*|└─*"), "   "),
            (re.compile(r"│"), " "),
        ]
    )

    comment_replacements: ReplacementRule = field(
        default_factory=lambda: [
            (re.compile(r"#.*$|\/\/.*$|--.*$|;.*$"), ""),
            (re.compile(r"\(.*\)$|\*.*$"), ""),
        ]
    )

    def clean_text(self, property: TextCleanerPro, text: str) -> str:
        rules: ReplacementRule = getattr(self, property.value)
        for rule in rules:
            text = re.sub(rule[0], rule[1], text)
        return text
