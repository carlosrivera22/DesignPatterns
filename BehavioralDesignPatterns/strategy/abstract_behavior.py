# Abstract Strategy
from abc import ABC, abstractmethod

class AbstractBehavior(ABC):

    @abstractmethod
    def move_command(self):
        pass


