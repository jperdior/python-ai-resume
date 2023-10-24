class Question:
    def __init__(
        self,
        id: str,
        question: str,
        answer: str,
        computingTokens: int,
        completionTokens: int,
        totalTokens: int,
    ):
        self.id = id
        self.question = question
        self.answer = answer
        self.computingTokens = computingTokens
        self.completionTokens = completionTokens
        self.totalTokens = totalTokens
