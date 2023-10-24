from api.domain.entities import Question
from api.infrastructure.storage.models import QuestionModel

class QuestionDataTransformer():

    @staticmethod
    def model_to_entity(question_model: QuestionModel) -> Question:
        return Question(
            id=question_model.id,
            question=question_model.question,
            answer=question_model.answer,
            computingTokens=question_model.computingTokens,
            completionTokens=question_model.completionTokens,
            totalTokens=question_model.totalTokens,
        )

    @staticmethod
    def entity_to_model(question: Question) -> QuestionModel:
        return QuestionModel(
            id=question.id,
            question=question.question,
            answer=question.answer,
            computingTokens=question.computingTokens,
            completionTokens=question.completionTokens,
            totalTokens=question.totalTokens,
        )