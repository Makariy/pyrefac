from rope.base.change import ChangeSet
from rope.base.project import Project
from rope.refactor.rename import Rename

from file_utils import path_to_module


def create_move_module_changes(project: Project, path: str, new_path: str) -> ChangeSet:
    resource = project.get_resource(path)
    rename = Rename(project, resource)
    return rename.get_changes(path_to_module(new_path))
