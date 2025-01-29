import os

import pytest
from unittest.mock import AsyncMock, patch

from langchain_openai import ChatOpenAI
from sqlalchemy.util import await_only


from llmtranslate import get_language_info, AsyncTranslator, TextLanguage, MissingLangchainChatModelError
from llmtranslate import Translator

# Test Translator
class TestTranslator:

    @pytest.fixture
    def translator(self):
        llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"))
        return Translator(llm=llm, max_translation_chunk_length=100, max_translation_chunk_length_multilang=100)

    def test_set_api_key_success(self, translator):
        assert translator.llm is not None

    def test_set_llm_failure(self):
        with pytest.raises(MissingLangchainChatModelError):
            Translator(llm=None)

    def test_translate_chunk_of_text(self, translator, mocker):
        # Create mock response
        mocked_llm_response = mocker.Mock()
        mocked_llm_response.translated_text = "translated text"

        # Create a mock for the entire LLM object
        mock_llm = mocker.Mock()
        mock_llm.invoke.return_value = mocked_llm_response

        # Replace the entire LLM object
        translator.few_shot_structured_llm_translate_text = mock_llm

        result = translator.translate_chunk_of_text("text", "en")
        assert result == "translated text"


    def test_get_text_language(self, translator, mocker):
        mocked_llm_response = mocker.Mock()
        mocked_llm_response.language_ISO_639_1_code = "en"

        mock_llm = mocker.Mock()
        mock_llm.invoke.return_value = mocked_llm_response

        translator.few_shot_structured_llm_count_number_of_languages_in_text = mock_llm
        result = translator.get_text_language("Some text")

        language_info = get_language_info("en")
        check_result = TextLanguage(language_info.get("ISO_639_1_code"))

        assert result == check_result


    def test_how_many_languages_are_in_text(self, translator, mocker):
        mocked_llm_response = mocker.Mock()
        mocked_llm_response.number_of_languages = 1

        mocked_llm = mocker.Mock()
        mocked_llm.invoke.return_value = mocked_llm_response

        translator.few_shot_structured_llm_count_number_of_languages_in_text= mocked_llm
        result = translator.how_many_languages_are_in_text("How many languages are in the text?")
        assert result == 1

    def test_translate(self, translator, mocker):
        ######### mocking number of languages
        mocked_llm_response_number_of_languages = mocker.Mock()
        mocked_llm_response_number_of_languages.number_of_languages = 1

        mocked_llm_number_of_languages = mocker.Mock()
        mocked_llm_number_of_languages.invoke.return_value = mocked_llm_response_number_of_languages

        translator.few_shot_structured_llm_count_number_of_languages_in_text = mocked_llm_number_of_languages

        mocked_llm_response_translate_text = mocker.Mock()
        mocked_llm_response_translate_text.translated_text = "Some text"

        mocked_llm_translate_text = mocker.Mock()
        mocked_llm_translate_text.invoke.return_value = mocked_llm_response_translate_text

        translator.few_shot_structured_llm_translate_text = mocked_llm_translate_text

        assert translator.translate("Some text", "en") == "Some text"

    def test_translate_number_of_languages_over_one(self, translator, mocker):
        ######### mocking number of languages
        mocked_llm_response_number_of_languages = mocker.Mock()
        mocked_llm_response_number_of_languages.number_of_languages = 2

        mocked_llm_number_of_languages = mocker.Mock()
        mocked_llm_number_of_languages.invoke.return_value = mocked_llm_response_number_of_languages

        translator.few_shot_structured_llm_count_number_of_languages_in_text = mocked_llm_number_of_languages

        mocked_llm_response_translate_text = mocker.Mock()
        mocked_llm_response_translate_text.translated_text = "Some text"

        mocked_llm_translate_text = mocker.Mock()
        mocked_llm_translate_text.invoke.return_value = mocked_llm_response_translate_text

        translator.few_shot_structured_llm_translate_text = mocked_llm_translate_text

        assert translator.translate("Some text", "en") == "Some text"




class TestAsyncTranslator:

    @pytest.fixture
    def translator(self):
        llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"))
        return AsyncTranslator(llm=llm, max_translation_chunk_length=100, max_translation_chunk_length_multilang=100, max_concurrent_llm_calls=10)

    def test_set_api_key_success(self, translator):
        assert translator.llm is not None

    @pytest.mark.asyncio
    async def test_translate_chunk_of_text(self, translator, mocker):
        # Create mock response
        mocked_llm_response =  mocker.Mock()
        mocked_llm_response.translated_text = "translated text"

        # Create a mock for the entire LLM object
        mock_llm = mocker.AsyncMock()
        mock_llm.ainvoke.return_value = mocked_llm_response

        # Replace the entire LLM object
        translator.few_shot_structured_llm_translate_text = mock_llm

        result = await translator.translate_chunk_of_text("text", "en")
        assert result == "translated text"

    @pytest.mark.asyncio
    async def test_get_text_language(self, translator, mocker):
        mocked_llm_response = mocker.Mock()
        mocked_llm_response.language_ISO_639_1_code = "en"

        mock_llm = mocker.AsyncMock()
        mock_llm.ainvoke.return_value = mocked_llm_response

        translator.few_shot_structured_llm_count_number_of_languages_in_text = mock_llm
        result = await translator.get_text_language("Some text")

        language_info = get_language_info("en")
        check_result = TextLanguage(language_info.get("ISO_639_1_code"))

        assert result == check_result

    @pytest.mark.asyncio
    async def test_how_many_languages_are_in_text(self, translator, mocker):
        mocked_llm_response = mocker.Mock()
        mocked_llm_response.number_of_languages = 1

        mocked_llm = mocker.AsyncMock()
        mocked_llm.ainvoke.return_value = mocked_llm_response

        translator.few_shot_structured_llm_count_number_of_languages_in_text= mocked_llm
        result = await translator.how_many_languages_are_in_text("How many languages are in the text?")
        assert result == 1


    @pytest.mark.asyncio
    async def test_translate(self, translator, mocker):
        ######### mocking number of languages
        mocked_llm_response_number_of_languages = mocker.Mock()
        mocked_llm_response_number_of_languages.number_of_languages = 1

        mocked_llm_number_of_languages = mocker.AsyncMock()
        mocked_llm_number_of_languages.ainvoke.return_value = mocked_llm_response_number_of_languages

        translator.few_shot_structured_llm_count_number_of_languages_in_text = mocked_llm_number_of_languages

        mocked_llm_response_translate_text = mocker.Mock()
        mocked_llm_response_translate_text.translated_text = "Some text"

        mocked_llm_translate_text = mocker.AsyncMock()
        mocked_llm_translate_text.ainvoke.return_value = mocked_llm_response_translate_text

        translator.few_shot_structured_llm_translate_text = mocked_llm_translate_text

        assert await translator.translate("Some text", "en") == "Some text"

    @pytest.mark.asyncio
    async def test_translate_number_of_languages_over_one(self, translator, mocker):
        ######### mocking number of languages
        mocked_llm_response_number_of_languages = mocker.Mock()
        mocked_llm_response_number_of_languages.number_of_languages = 2

        mocked_llm_number_of_languages = mocker.AsyncMock()
        mocked_llm_number_of_languages.ainvoke.return_value = mocked_llm_response_number_of_languages

        translator.few_shot_structured_llm_count_number_of_languages_in_text = mocked_llm_number_of_languages

        mocked_llm_response_translate_text = mocker.Mock()
        mocked_llm_response_translate_text.translated_text = "Some text"

        mocked_llm_translate_text = mocker.AsyncMock()
        mocked_llm_translate_text.ainvoke.return_value = mocked_llm_response_translate_text

        translator.few_shot_structured_llm_translate_text = mocked_llm_translate_text

        assert await translator.translate("Some text", "en") == "Some text"





