from api.domain.entities import Question
from api.domain.repository.question_repository import QuestionRepositoryInterface
from api.domain.factories import QuestionFactory

class QuestionUseCases():

    def __init__(self, repository: QuestionRepositoryInterface):
        self.repository = repository
        
    def create(self, question: str):
        question = QuestionFactory.create_question(question=question)
        return self.repository.save(question)