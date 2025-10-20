from abc import ABC, abstractmethod

class ILogger(ABC):
    """
    Interface for logging systems
    Allows different logging implementations (fila, console, database, etc.)
    """

    @abstractmethod
    def log(self, message:str) -> None:
        """ Logs a message to the chosen output."""
        pass