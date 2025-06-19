from typing import cast
from rope.base.change import ChangeSet
from rope.base.project import Project
from rope.base.pyobjectsdef import PyModule
from rope.refactor.move import MoveModule

from file_utils import path_to_module
from change.create_directory_if_not_exists import CreatePackageIfNotExistsChange


def create_move_module_changes(
    project: Project,
    src_path: str,
    dest_path: str
) -> ChangeSet:
    changes = ChangeSet("Move module")
    changes.add_change(CreatePackageIfNotExistsChange(project, dest_path))

    module: PyModule = cast(PyModule, project.get_module(path_to_module(src_path)))

    move = MoveModule(project, module.get_resource())
    changes.add_change(
        move.get_changes(project.get_resource(dest_path))
    )

    return changes

