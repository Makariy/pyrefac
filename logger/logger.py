from typing import override
from abc import ABC, abstractmethod

from rope.base.resources import Resource
from rope.base.change import Change, ChangeSet


class IChangeLogger(ABC):
    @abstractmethod
    def log_changes(self, changes: ChangeSet) -> None:
        pass


class MockChangeLogger(IChangeLogger):
    @override
    def log_changes(self, changes: ChangeSet) -> None:
        return


class ConsoleChangeLogger(IChangeLogger):
    @override
    def log_changes(self, changes: ChangeSet) -> None:
        print(changes.get_description())


class FilesChangeLogger(IChangeLogger):
    @override
    def log_changes(self, changes: ChangeSet) -> None:
        files: list[str] = []

        change: Change
        for change in changes.changes:
            resource: Resource
            for resource in change.get_changed_resources():
                if resource.is_dir():
                    continue
                files.append(resource.path)

        print(",".join(files))
