import asyncio
import os

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from llmtranslate import AsyncTranslator
from llmtranslate.benchmark.short_benchmark import run_short_benchmark_formated_output

llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"))
llmv2 = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    max_retries=2,
)
translator = AsyncTranslator(
    llm=llm,
    max_translation_chunk_length=100,
    max_translation_chunk_length_multilang=100,
    max_concurrent_llm_calls = 50,
    max_concurrent_time_period = 60,
)


print(asyncio.run(run_short_benchmark_formated_output("claude-3-5-sonnet-20240620", translator, llmv2,"pl")))