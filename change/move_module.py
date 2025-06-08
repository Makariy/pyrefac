from rope.base.change import ChangeSet
from rope.base.project import Project
from rope.refactor.rename import Rename

from file_utils import remove_extension


def create_move_module_changes(
    project: Project, path: str, new_filename: str
) -> ChangeSet:
    resource = project.get_resource(path)
    rename = Rename(project, resource)
    return rename.get_changes(remove_extension(new_filename))
