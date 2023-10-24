from abc import ABC, abstractmethod


class ArtificialIntelligenceProviderInterface(ABC):
    @abstractmethod
    def prompt(self, question: str) -> str:
        pass
