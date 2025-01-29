import os
from llmtranslate import Translator
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=os.getenv("OPENAI_API_KEY"))
translator = Translator(llm=llm, max_translation_chunk_length=100, max_translation_chunk_length_multilang=100)
text_language = translator.get_text_language("Hi how are you?")
if text_language:
    print(text_language.ISO_639_1_code)
    print(text_language.ISO_639_2_code)
    print(text_language.ISO_639_3_code)
    print(text_language.language_name)

print(translator.translate("Hi how are you?", "Spanish"))


