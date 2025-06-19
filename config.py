from dataclasses import dataclass
from enum import Enum


class RefactorAction(Enum):
    MOVE_SYMBOL = "move-symbol"
    RENAME_MODULE = "rename-module"
    MOVE_MODULE = "move-module"


@dataclass
class MoveSymbolConfig:
    source: str
    symbol: str
    dest: str


@dataclass
class RenameModuleConfig:
    source: str
    dest: str


@dataclass 
class MoveModuleConfig:
    source: str 
    dest: str


@dataclass
class RefactorConfig:
    action: RefactorAction
    config: RenameModuleConfig | MoveSymbolConfig | MoveModuleConfig
    is_dry_run: bool
    is_verbose: bool
    show_files: bool
    project_root: str
    excluded_files: list[str]

