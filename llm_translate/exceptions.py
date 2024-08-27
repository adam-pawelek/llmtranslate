from llm_translate.utils.enums import ModelForTranslator


class MissingAPIKeyError(Exception):
    """Exception raised for missing API key."""
    def __init__(self, message="OpenAI API key is not set. Please set the API key using the instructions in the documentation. See: https://github.com/adam-pawelek/SimpleAITranslator?tab=readme-ov-file#setting-the-openai-api-key"):
        self.message = message
        super().__init__(self.message)


class NoneAPIKeyProvidedError(Exception):
    """Exception raised for missing API key."""
    def __init__(self, message="Provide a valid API key. Right now you passed None value to this function"):
        self.message = message
        super().__init__(self.message)


class InvalidModelName(Exception):
    """Exception raised for invalid model name."""
    def __init__(self, message="", invalid_model_name=None):
        valid_models = ", ".join(model.value for model in ModelForTranslator)
        self.message = f"Invalid model name '{invalid_model_name}'. Value must be one of: {valid_models}"
        super().__init__(self.message)


