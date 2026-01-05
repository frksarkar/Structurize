from pathlib import Path
from dataclasses import dataclass, field
from Type import RunMode, ConfigType
import yaml
from typing import cast


@dataclass()
class Config:
    # default value defined
    _current_file_path: Path = Path(__file__).resolve().parent
    _base_path: Path = _current_file_path.parent
    _default_config_path: Path = Path(__file__).resolve().parent / "config.yaml"
    _output_dir: Path = field(default=Path("generated_project"))
    _working_dir: Path = field(default=Path("structure"))
    _file_path: Path = field(default=Path("structure.tree"))
    _INVALID_FILENAMES = frozenset(
        [
            ".",
            "..",
            "...",
            "con",
            "prn",
            "aux",
            "nul",
            "com1",
            "com2",
            "com3",
            "com4",
            "com5",
            "com6",
            "com7",
            "com8",
            "com9",
        ]
    )
    doc_separator = "/"

    @property
    def file_path(self) -> Path:
        return self.base_path / self._working_dir / self._file_path

    @property
    def base_path(self):
        return self._base_path

    @property
    def output_dir(self):
        return self.base_path / self._output_dir

    @property
    def working_dir(self):
        return self.base_path / self._working_dir

    @base_path.setter
    def base_path(self, pathname: Path):
        self._base_path = Path(pathname).resolve()

    @output_dir.setter
    def output_dir(self, output_dir: str):
        self._output_dir = Path(output_dir)

    @working_dir.setter
    def working_dir(self, working_dir: str):
        self._working_dir = Path(working_dir)

    @file_path.setter
    def file_path(self, file_path: str):
        self._file_path = self.base_path / self._working_dir / file_path

    # behavior config
    mode: RunMode = field(default=RunMode.NORMAL, init=False)  # RunMode.DRY_RUN
    multi_file_mode: bool = True
    invalid_filenames: frozenset[str] = field(default=_INVALID_FILENAMES, init=False)
    indent: int = 4

    def __post_init__(self):
        self.load_config()


    def load_config(self):
        if not self._default_config_path.exists():
            return print('"config.yaml" not found', self._default_config_path)

        with open(self._default_config_path, "r", encoding="utf-8") as f:
            loadConfig: ConfigType = yaml.safe_load(f)
        self.loop_config(loadConfig)

    def loop_config(self, loadConfig: ConfigType):
        for key, value in loadConfig.items():
            if isinstance(value, dict) or isinstance(value, list):
                self.loop_config(cast(ConfigType, value))
                continue
            setattr(self, key, value)


