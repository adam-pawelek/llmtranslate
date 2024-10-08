from enum import Enum


class ModelForTranslator(Enum):
    BEST_BIG_MODEL = "gpt-4o"
    BEST_SMALL_MODEL = "gpt-4o-mini"
    GPT_4o = "gpt-4o"
    GPT_4o_mini = "gpt-4o-mini"
    MISTRAL_LARGE = "mistral-large-latest"
    MISTRAL_NEMO = "open-mistral-nemo"

    def __str__(self):
        return self.value