import asyncio
import os

from llmtranslate import TranslatorOpenAI, TranslatorOpenSource, TranslatorMistralCloud
from llmtranslate.benchmark.benchmark_core import check_translation_to_language_using_original_text, \
    get_supported_languages_translation_using_original_text, benchmark_translation_to_language_using_original_text, \
    create_readme_format, get_supported_languages_from_benchmark_results
from llmtranslate.benchmark.data.short_text_data import test_data_short_benchmark_learning_new_language


async def benchmark_short_text_translation(translator, language_to_check):
    original_text = ""
    for text, language_code in test_data_short_benchmark_learning_new_language:
        if language_code == language_to_check:
            original_text = text

    if original_text == "":
        raise ValueError("This language is not supported by this benchmark.")


    benchmark_result = await benchmark_translation_to_language_using_original_text(
        translator=translator,
        language_list_to_translate= test_data_short_benchmark_learning_new_language,
        language_to_check=language_to_check,
        original_text="Learning a new language can be challenging, but it is also exciting. It helps us connect with people from different cultures and understand the world better. Every new language we learn gives us a fresh perspective and opens up new opportunities."
    )
    return benchmark_result


#translator_to_test = TranslatorOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")
'''
translator = TranslatorOpenSource(
    api_key=os.environ.get("YOUR_HF_TOKEN"),
    llm_endpoint="https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407/v1",
    model="meta-llama/Llama-3.2-3B-Instruct",
    model_size="mini"
)
'''

translator = TranslatorMistralCloud(os.getenv("MISTRAL_API_KEY"), "ministral-8b-latest")


benchmark_result = asyncio.run(benchmark_short_text_translation(translator,"en"))

supported_languages = get_supported_languages_from_benchmark_results(benchmark_result)

print(supported_languages)

print(benchmark_result)

print(create_readme_format("Nemo",benchmark_result))
print("\n\n\n--------------------------------------------------------")
print(create_readme_format("Nemo", supported_languages))



