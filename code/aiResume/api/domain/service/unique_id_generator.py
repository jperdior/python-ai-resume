from abc import ABC, abstractmethod

class UniqueIdGeneratorInterface(ABC):

    @abstractmethod
    def generateUlid(self) -> str:
        pass