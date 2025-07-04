from typing import cast
import os

from rope.base.project import Project
from rope.base.resources import File, Folder
from rope.base.pyobjects import PyModule
from rope.base.exceptions import ResourceNotFoundError


def path_to_module(path: str) -> str:
    return path.removesuffix(".py").replace("/", ".")


def module_to_path(module: str) -> str:
    return module.replace(".", "/") + ".py"


def remove_extension(path: str) -> str:
    return path.removesuffix(".py")


def _create_project_file(project: Project, filename: str) -> None:
    path = os.path.join(project.root.path, filename)
    with open(path, "w") as f:
        f.write("")


def _create_project_package(project: Project, directory: str) -> None:
    path = os.path.join(project.root.path, directory)
    os.mkdir(directory)
    with open(os.path.join(path, "__init__.py")) as f:
        f.write("")


def get_or_create_file_resource(project: Project, filename: str) -> File:
    try:
        return cast(File, project.get_resource(filename))
    except ResourceNotFoundError:
        _create_project_file(project, filename)
        return cast(File, project.get_file(filename))

def get_or_create_package_resource(project: Project, directory: str) -> Folder:
    try:
        return cast(Folder, project.get_resource(directory))
    except ResourceNotFoundError:
        _create_project_package(project, directory)
        return cast(Folder, project.get_resource(directory))


def get_module_string_content(module: PyModule) -> str:
    res = module.get_resource()
    with open(res.real_path, "r") as f:
        return f.read()
