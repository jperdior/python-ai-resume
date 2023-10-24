from api.domain.entities import Question
from api.domain.repository.question_repository import QuestionRepositoryInterface
from api.infrastructure.storage.models import QuestionModel
from api.application.data_transformer.question_data_transformers import QuestionDataTransformer

class QuestionRepository(QuestionRepositoryInterface):

    def __init__(self):
        self.model = QuestionModel

    def save(self, question: Question):
        question_model = QuestionDataTransformer.entity_to_model(question)
        return super().save(question_model)   