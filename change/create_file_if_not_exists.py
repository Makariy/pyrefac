from typing import override 
from rope.base.change import Change
from rope.base.project import Project 
from file_utils import (
    get_or_create_file_resource
)


class CreateFileIfNotExistsChange(Change):
    def __init__(self, project: Project, path: str) -> None:
        super().__init__()
        _ = get_or_create_file_resource(
            project,
            path
        )


    @override
    def do(self, job_set=None):
        return super().do(job_set)

    @override 
    def undo(self, job_set=None):
        raise NotImplemented



