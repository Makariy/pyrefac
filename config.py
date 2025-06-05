from dataclasses import dataclass
from enum import Enum


class RefactorAction(Enum):
    MOVE_SYMBOL = "move-symbol"
    RENAME_MODULE = "rename-module"


@dataclass
class RenameModuleConfig:
    source: str
    dest: str


@dataclass
class MoveSymbolConfig:
    source: str
    symbol: str
    dest: str


@dataclass
class RefactorConfig:
    action: RefactorAction
    config: RenameModuleConfig | MoveSymbolConfig
    is_dry_run: bool
    is_verbose: bool

