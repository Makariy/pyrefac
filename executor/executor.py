from typing import override
from abc import ABC, abstractmethod 

from rope.base.project import Project
from rope.base.change import ChangeSet


class IChangeExecutor(ABC):
    @abstractmethod
    def execute(self, project: Project, changes: ChangeSet) -> None:
        pass 


class MockChangeExecutor(IChangeExecutor):
    @override
    def execute(self, project: Project, changes: ChangeSet) -> None:
        return 


class ChangeExecutor(IChangeExecutor):
    @override
    def execute(self, project: Project, changes: ChangeSet) -> None:
        project.do(changes)

