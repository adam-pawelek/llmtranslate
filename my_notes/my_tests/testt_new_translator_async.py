import asyncio
import os
from langchain_openai import ChatOpenAI

from llmtranslate import AsyncTranslator

llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=os.getenv("OPENAI_API_KEY"))
async def translate_text():
    translator = AsyncTranslator(llm=llm, max_translation_chunk_length=100, max_translation_chunk_length_multilang=50, max_concurrent_llm_calls=10)
    tasks = [translator.get_text_language("Hi how are you?"), translator.translate("Hi how are you?", "Spanish")]
    results = await asyncio.gather(*tasks)
    print(results[0])
    print(results[1])

asyncio.run(translate_text())
