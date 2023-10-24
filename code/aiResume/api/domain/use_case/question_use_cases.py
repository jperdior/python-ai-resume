from api.domain.entities import Question
from api.domain.repository.question_repository import QuestionRepositoryInterface
from api.domain.factories import QuestionFactory

class QuestionUseCases():

    def __init__(self, repository: QuestionRepositoryInterface, questionFactory: QuestionFactory):
        self.repository = repository
        self.questionFactory = questionFactory
        
    def create(self, question: str) -> Question:
        question = self.questionFactory.create_question(question=question)
        return self.repository.save(question)