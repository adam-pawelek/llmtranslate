import os
from llmtranslate import Translator
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=os.getenv("OPENAI_API_KEY"))
translator = Translator(llm=llm, max_length_text_chunk_to_translate=100, max_length_text_chunk_to_translate_multiple_languages=100)
text_language = translator.get_text_language("Hi how are you?")
if text_language:
    print(text_language.ISO_639_1_code)
    print(text_language.ISO_639_2_code)
    print(text_language.ISO_639_3_code)
    print(text_language.language_name)

print(translator.translate("Hi how are you?", "Spanish"))


