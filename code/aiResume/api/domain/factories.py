import ulid
from api.domain.entities import Question

class QuestionFactory():
    """
    QuestionFactory class
    """
    @staticmethod
    def create_question(question:str) -> Question:
        """
        create_question method
        """
        return Question(id=str(ulid.new()), question=question, answer="", computingTokens=0, completionTokens=0, totalTokens=0)
        