import asyncio
import os
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from llmtranslate import AsyncTranslator, get_language_info
from llmtranslate.benchmark.benchmark_core import benchmark_one_text
from llmtranslate.benchmark.data.short_text import short_benchmark_text_for_translation
from llmtranslate.benchmark.format_benchmark_output import create_readme_format


async def run_short_benchmark(translator: AsyncTranslator, llm_to_check_translation: BaseChatModel, to_language: str):
    return await benchmark_one_text(
        translator= translator,
        chat_model_to_check_translation=llm_to_check_translation,
        sentences_in_different_languages=short_benchmark_text_for_translation,
        translate_to_lang=get_language_info(to_language)["language_name"],
        expected_translation=short_benchmark_text_for_translation[to_language]
    )


async def run_short_benchmark_formated_output(llm_model_name, translator, llm_to_check_translation, to_language):
    benchmark_results = await run_short_benchmark(translator, llm_to_check_translation, to_language)

    return  create_readme_format(llm_model_name, benchmark_results)

