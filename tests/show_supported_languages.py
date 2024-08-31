import os
import llmtranslate
from llmtranslate.translator import TranslatorOpenAI
#from llmtranslate.translator import how_many_languages_are_in_text



translator = TranslatorOpenAI(os.environ.get("OPENAI_API_KEY"))
print(translator.supported_languages.languages.languages_full_data[0].iso_639_3_code)


