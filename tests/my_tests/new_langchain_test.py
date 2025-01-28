import asyncio
import os
import getpass

from llmtranslate import  AsyncTranslator

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

translator = AsyncTranslator(llm=llm, max_length_text_chunk_to_translate=100, max_length_text_chunk_to_translate_multiple_languages=100)


async def run_test():
    print(await translator.get_text_language("Hi how are you?"))
    print(await translator.translate("Hi how are you?", "pl"))


asyncio.run(run_test())

