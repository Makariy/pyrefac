from typing import cast
from rope.base.change import ChangeSet
from rope.base.project import Project 
from rope.base.pyobjectsdef import PyModule
from rope.refactor.move import MoveGlobal
from ast_utils import (
    get_offset_for_function,
)
from .create_file_if_not_exists import CreateFileIfNotExistsChange


def create_move_function_changes(
    project: Project,
    src_module: str,
    func_name: str,
    dest_path: str 
) -> ChangeSet:
    changes = ChangeSet("Move function")
    changes.add_change(CreateFileIfNotExistsChange(project, dest_path))

    module: PyModule = cast(
        PyModule,
        project.get_module(src_module.removesuffix(".py"))
    )
    offset = get_offset_for_function(module, func_name)

    move = MoveGlobal(
        project,
        module.get_resource(),
        offset 
    )
    changes.add_change(move.get_changes(dest_path.removesuffix(".py")))
    return changes


