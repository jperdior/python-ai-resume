from api.application.handler.question_handler import QuestionHandler
from api.domain.use_case.question_use_cases import QuestionUseCases
from api.infrastructure.storage.repository.question_repository import QuestionRepository

QUESTION_REPOSITORY = QuestionRepository()
QUESTION_USE_CASES = QuestionUseCases(repository=QUESTION_REPOSITORY)
QUESTION_HANDLER = QuestionHandler(question_use_cases=QUESTION_USE_CASES)