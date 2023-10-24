from api.domain.service.unique_id_generator import UniqueIdGeneratorInterface
from api.domain.entities import Question

class QuestionFactory:
    
    def __init__(self, uniqueIdGenerator: UniqueIdGeneratorInterface):
        self.uniqueIdGenerator = uniqueIdGenerator

    def create_question(self, question:str) -> Question:
        return Question(id=self.uniqueIdGenerator.generateUlid(), question=question, answer="", computingTokens=0, completionTokens=0, totalTokens=0)
        