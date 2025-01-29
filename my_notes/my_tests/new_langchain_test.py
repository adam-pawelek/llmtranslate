import asyncio
import os
import getpass

from llmtranslate import  AsyncTranslator

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

translator = AsyncTranslator(llm=llm, max_translation_chunk_length=100, max_translation_chunk_length_multilang=100)


async def run_test():
    print(await translator.get_text_language("Hi how are you?"))
    print(await translator.translate("Hi how are you?", "pl"))


asyncio.run(run_test())

