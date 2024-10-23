import os

from llmtranslate import TranslatorOpenAI
from llmtranslate.benchmark.benchmark_core import check_translation_to_language_using_original_text, \
    get_supported_languages_translation_using_original_text, benchmark_translation_to_language_using_original_text
from llmtranslate.benchmark.data.short_text_data import test_data_short_benchmark_learning_new_language


def benchmark_short_text_translation(translator, language_to_check):
    original_text = ""
    for text, language_code in test_data_short_benchmark_learning_new_language:
        if language_code == language_to_check:
            original_text = text

    if original_text == "":
        raise ValueError("This language is not supported by this benchmark.")


    benchmark_result = benchmark_translation_to_language_using_original_text(
        translator=translator,
        language_list_to_translate= test_data_short_benchmark_learning_new_language,
        language_to_check=language_to_check,
        original_text="en"
    )
    return benchmark_result


translator_to_test = TranslatorOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")


print(benchmark_short_text_translation(translator_to_test,"en"))

