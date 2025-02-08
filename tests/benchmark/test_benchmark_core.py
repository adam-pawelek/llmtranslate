
from llmtranslate.benchmark.benchmark_core import check_if_translation_is_accurate




# Define a fake response that mimics the expected output.
class FakeLLMResponse:
    is_this_translation_accurate = "true"

# Make your fake structured LLM callable.
class FakeStructuredLLM:
    async def ainvoke(self, input_dict):
        return FakeLLMResponse()

    # Implement __call__ so that the object is callable.
    async def __call__(self, input_dict):
        return await self.ainvoke(input_dict)

# Your fake chat model returns a fake structured LLM.
class FakeChatModel:
    def with_structured_output(self, output_cls):
        # Return an instance of the callable FakeStructuredLLM.
        return FakeStructuredLLM()

# And a fake translator (if needed).
class FakeTranslator:
    async def translate(self, text, target_lang):
        return "translated text"

import pytest


@pytest.mark.asyncio
async def test_check_if_translation_is_accurate():
    fake_chat_model = FakeChatModel()
    fake_translator = FakeTranslator()

    result = await check_if_translation_is_accurate(
        chat_model_to_check_translation=fake_chat_model,
        translator=fake_translator,
        text_to_translate="Hello",
        source_lang="en",
        translate_to_lang="es",
        expected_translation="Hola"
    )

    # Assert that our fake response is reflected in the result.
    assert result["supported_language"] == "true"