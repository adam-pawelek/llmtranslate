import asyncio
import getpass
import os
from typing import Optional

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

from typing import Optional

from pydantic import BaseModel, Field


# Pydantic
class TranslateFormat(BaseModel):
    translated_text: str


structured_llm_translate_text = llm.with_structured_output(TranslateFormat)


from langchain_core.prompts import ChatPromptTemplate

translate_text_prompt_template = "You are a language translator. You should translate text provided by user to the {to_language} language. Don't write additional message like This is translated text just translate text."

translate_text_prompt = ChatPromptTemplate.from_messages([("system", translate_text_prompt_template), ("human", "{input}")])

few_shot_structured_llm = translate_text_prompt | structured_llm_translate_text
print(few_shot_structured_llm.invoke({"to_language": "Spanish", "input":"Czesc jak sie masz?"}))

#print(type(few_shot_structured_llm.invoke("what's something funny about woodpeckers")))


