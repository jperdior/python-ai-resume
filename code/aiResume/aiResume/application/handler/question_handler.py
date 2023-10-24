from domain.use_case.question_use_cases import QuestionUseCases
from api.v1.serializer.question_serializer import GetQuestionSerializer


class QuestionHandler():
    
        def __init__(self):
            self.question_use_cases = QuestionUseCases()
    
        def post_question(self, question: str) -> GetQuestionSerializer:
            return self.question_use_cases.create(question)

    