import pytest
from unittest.mock import AsyncMock, patch
from llmtranslate.exceptions import MissingAPIKeyError, NoneAPIKeyProvidedError, InvalidModelName
from llmtranslate import ModelForTranslator
from llmtranslate import Translator, TranslatorOpenAI, TranslatorAzureOpenAI

# Test TranslatorOpenAI
class TestTranslatorOpenAI:

    @pytest.fixture
    def translator(self):
        return TranslatorOpenAI(api_key="test_key")

    def test_set_api_key_success(self, translator):
        assert translator.client is not None

    def test_set_api_key_failure(self):
        with pytest.raises(NoneAPIKeyProvidedError):
            TranslatorOpenAI(api_key=None)

    def test_set_llm_success(self, translator):
        translator._set_llm(ModelForTranslator.BEST_BIG_MODEL.value)
        assert translator.model == ModelForTranslator.BEST_BIG_MODEL.value



    @pytest.mark.asyncio
    async def test_translate_chunk_of_text(self, translator):
        translator.client = AsyncMock()
        translator.client.beta.chat.completions.parse = AsyncMock(return_value=AsyncMock(
            choices=[AsyncMock(message=AsyncMock(parsed=AsyncMock(translated_text="translated text")))]
        ))

        result = await translator.translate_chunk_of_text("text", "en")
        assert result == "translated text"

    @pytest.mark.asyncio
    async def test_translate_chunk_of_text_no_client(self):
        translator = TranslatorOpenAI(api_key="test_key")
        translator.client = None
        with pytest.raises(MissingAPIKeyError):
            await translator.translate_chunk_of_text("text", "en")


# Test TranslatorAzureOpenAI
class TestTranslatorAzureOpenAI:

    @pytest.fixture
    def translator(self):
        return TranslatorAzureOpenAI(azure_endpoint="https://test.endpoint",
                                     api_key="test_key",
                                     api_version="v1",
                                     azure_deployment="test_deployment")

    def test_set_api_key_success(self, translator):
        assert translator.client is not None

    def test_set_api_key_failure(self):
        with pytest.raises(NoneAPIKeyProvidedError):
            TranslatorAzureOpenAI(azure_endpoint="https://test.endpoint",
                                  api_key=None,
                                  api_version="v1",
                                  azure_deployment="test_deployment")

    def test_set_llm_success(self, translator):
        translator._set_llm(ModelForTranslator.BEST_BIG_MODEL.value)
        assert translator.model == ModelForTranslator.BEST_BIG_MODEL.value



# Test Translator class methods
class TestTranslatorMethods:

    @pytest.fixture
    def translator(self):
        return TranslatorOpenAI(api_key="test_key")

    @pytest.mark.asyncio
    async def test_async_get_text_language(self, translator):
        translator.client = AsyncMock()
        translator.client.beta.chat.completions.parse = AsyncMock(return_value=AsyncMock(
            choices=[AsyncMock(message=AsyncMock(parsed=AsyncMock(language_ISO_639_1_code="en")))]
        ))

        result = await translator.async_get_text_language("Hello world")
        assert result.ISO_639_1_code == "en"

    def test_get_text_language(self, translator):
        with patch.object(TranslatorOpenAI, 'async_get_text_language',
        return_value=Translator.TextLanguage(
            ISO_639_1_code="en",
            ISO_639_2_code="eng",
            ISO_639_3_code="eng",
            language_name="English"
        )) as mock_async_method:
            result = translator.get_text_language("Hello world")
            assert result.ISO_639_1_code == "en"
            assert result.language_name == "English"
            mock_async_method.assert_called_once()

    @pytest.mark.asyncio
    async def test_async_translate(self, translator):
        # Mocking the client and the response for translate_chunk_of_text
        translator.client = AsyncMock()
        translator.client.beta.chat.completions.parse = AsyncMock(return_value=AsyncMock(
            choices=[AsyncMock(message=AsyncMock(parsed=AsyncMock(translated_text="translated text")))]
        ))

        # Mocking the how_many_languages_are_in_text to return an integer
        translator.how_many_languages_are_in_text = AsyncMock(return_value=1)

        result = await translator.async_translate("Hello world", "en")

        assert result == "translated text"

    def test_translate(self, translator):
        with patch.object(TranslatorOpenAI, 'async_translate', return_value="translated text") as mock_async_method:
            result = translator.translate("Hello world", "en")
            assert result == "translated text"
            mock_async_method.assert_called_once()

    @pytest.mark.asyncio
    async def test_how_many_languages_are_in_text(self, translator):
        translator.client = AsyncMock()
        translator.client.beta.chat.completions.parse = AsyncMock(return_value=AsyncMock(
            choices=[AsyncMock(message=AsyncMock(parsed=AsyncMock(number_of_languages=2)))]
        ))

        result = await translator.how_many_languages_are_in_text("Hello world")
        assert result == 2
