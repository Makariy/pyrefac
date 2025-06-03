from typing import override
from abc import ABC, abstractmethod 

from rope.base.change import ChangeSet


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


