import os
import getpass

from llmtranslate import Translator

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

translator = Translator(llm=llm, max_length=100,max_length_mini_text_chunk=100)

print(translator.get_text_language("Hi how are you?"))




print(translator.translate("Hi how are you?", "pl"))


