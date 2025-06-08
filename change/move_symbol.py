from typing import cast
from rope.base.change import ChangeSet
from rope.base.project import Project
from rope.base.pyobjectsdef import PyModule
from rope.refactor.move import MoveGlobal

from ast_utils import get_offset_for_symbol
from file_utils import path_to_module
from .create_file_if_not_exists import CreateFileIfNotExistsChange


def create_move_symbol_changes(
    project: Project, src_path: str, symbol_name: str, dest_path: str
) -> ChangeSet:
    changes = ChangeSet("Move symbols")
    changes.add_change(CreateFileIfNotExistsChange(project, dest_path))

    module: PyModule = cast(PyModule, project.get_module(path_to_module(src_path)))
    offset = get_offset_for_symbol(module, symbol_name)

    move = MoveGlobal(project, module.get_resource(), offset)
    changes.add_change(move.get_changes(path_to_module(dest_path)))

    return changes
