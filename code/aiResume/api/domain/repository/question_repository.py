from abc import ABC, abstractmethod
from api.domain.entities import Question


class QuestionRepositoryInterface(ABC):
    @abstractmethod
    def save(self, question: Question):
        pass
