from api.domain.entities import Question
from api.domain.repository.question_repository import QuestionRepositoryInterface
from api.domain.factories import QuestionFactory
from api.domain.artificial_intelligence import ArtificialIntelligenceProviderInterface


class QuestionUseCases:
    def __init__(
        self,
        repository: QuestionRepositoryInterface,
        questionFactory: QuestionFactory,
        artificialIntelligence: ArtificialIntelligenceProviderInterface,
    ):
        self.repository = repository
        self.questionFactory = questionFactory
        self.artificialIntelligence = artificialIntelligence

    def create(self, question: str) -> Question:
        question = self.questionFactory.create_question(question=question)
        question = self.artificialIntelligence.prompt(question=question)
        return self.repository.save(question)
