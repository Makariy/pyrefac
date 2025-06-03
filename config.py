from dataclasses import dataclass
from enum import Enum


class RefactorAction(Enum):
    MOVE_FUNC = "move-func"
    MOVE_CLASS = "move-class"
    RENAME_MODULE = "rename-module"


@dataclass
class RenameModuleConfig:
    source: str
    dest: str


@dataclass
class MoveClassConfig:
    source: str
    class_name: str
    dest: str


@dataclass
class MoveFuncConfig:
    source: str
    func_name: str
    dest: str


@dataclass
class RefactorConfig:
    action: RefactorAction
    config: RenameModuleConfig | MoveClassConfig | MoveFuncConfig
    is_dry_run: bool
    is_verbose: bool

