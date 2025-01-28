import os
from llmtranslate import Translator
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=os.getenv("OPENAI_API_KEY"))
translator = Translator(llm=llm, max_length_text_chunk_to_translate=100, max_length_text_chunk_to_translate_multiple_languages=100)
print(translator.get_text_language("Hi how are you?"))
print(translator.translate("Hi how are you?", "Spanish"))


