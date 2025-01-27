import pytest
from unittest.mock import AsyncMock, patch

from langchain_openai import ChatOpenAI

from llmtranslate.exceptions import MissingAPIKeyError, NoneAPIKeyProvidedError, InvalidModelName
from llmtranslate import ModelForTranslator
from llmtranslate import Translator

# Test Translator
class TestTranslator:

    @pytest.fixture
    def translator(self):
        llm = ChatOpenAI(model="gpt-4o-mini")
        return Translator(llm=llm, max_length=100, max_length_mini_text_chunk=100)

    def test_set_api_key_success(self, translator):
        assert translator.llm is not None

    def test_translate_chunk_of_text(self, translator, mocker):
        # Create mock response
        mock_response = mocker.Mock()
        mock_response.translated_text = "translated text"

        # Create a mock for the entire LLM object
        mock_llm = mocker.Mock()
        mock_llm.invoke.return_value = mock_response

        # Replace the entire LLM object
        translator.few_shot_structured_llm_translate_text = mock_llm

        result = translator.translate_chunk_of_text("text", "en")
        assert result == "translated text"



