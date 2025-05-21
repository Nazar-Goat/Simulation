from abc import ABC, abstractmethod

class Action(ABC):
    """Abstract base class for all actions"""

    @abstractmethod
    def execute(self, map_obj):
        pass