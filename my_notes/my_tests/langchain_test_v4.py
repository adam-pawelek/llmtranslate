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
class HowManyLanguages(BaseModel):
    number_of_languages: int


structured_llm_count_number_of_languages_in_text= llm.with_structured_output(HowManyLanguages)


from langchain_core.prompts import ChatPromptTemplate

count_number_of_languages_in_text_prompt_template = "You are text languages counter you should count how many languages are in provided by user text"

count_number_of_languages_in_text_prompt = ChatPromptTemplate.from_messages([("system", count_number_of_languages_in_text_prompt_template), ("human", "{input}")])

few_shot_structured_llm = count_number_of_languages_in_text_prompt | structured_llm_count_number_of_languages_in_text
print(few_shot_structured_llm.invoke({"Czesc jak sie masz Hi how are you?"}))

#print(type(few_shot_structured_llm.invoke("what's something funny about woodpeckers")))


