from domain.entities import Question
from domain.repository.question_repository import QuestionRepositoryInterface

class QuestionUseCases():

    def __init__(self):
        self.repository = QuestionRepositoryInterface()

    def create(self, question: str):
        question = Question(question=question, answer="", computingTokens=0, completionTokens=0, totalTokens=0)
        return self.repository.save(question)