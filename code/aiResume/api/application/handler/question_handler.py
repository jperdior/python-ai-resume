from api.domain.use_case.question_use_cases import QuestionUseCases
from api.presentation.v1.serializer.question_serializer import GetQuestionSerializer
from django.db import transaction
import logging


class QuestionHandler():
    
        def __init__(self, question_use_cases: QuestionUseCases):
            self.question_use_cases = question_use_cases
    
        def create_question(self, question: str) -> GetQuestionSerializer:
            try:
                with transaction.atomic():
                    logging.info("Creating question")
                    result = self.question_use_cases.create(question)
                return result
            except Exception as e:
                logging.error("Error creating question: " + str(e))
                raise e
                

    