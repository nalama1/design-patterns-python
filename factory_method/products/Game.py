from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def start(self):
        pass