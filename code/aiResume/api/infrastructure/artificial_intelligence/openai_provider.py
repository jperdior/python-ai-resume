import openai
from openai.embeddings_utils import get_embedding
from api.domain.artificial_intellingence.artificial_intelligence_provider import (
    ArtificialIntelligenceProviderInterface,
)


class OpenAiProvider(ArtificialIntelligenceProviderInterface):
    def __init__(self):
        self.openai = openai
        self.openai.api_key = "OPENAI_API_KEY"

    def prompt(self, prompt: str) -> str:
        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].text
