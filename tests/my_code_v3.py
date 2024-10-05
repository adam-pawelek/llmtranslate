import os

from llmtranslate import TranslatorOpenAI

# Initialize the translator with your OpenAI API key
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="o1-preview")

# Detect language
detected_language = translator.get_text_language("jak ty się nazywasz")
if detected_language is not None:
  print(detected_language.ISO_639_1_code)  # Output: 'pl'
  print(detected_language.ISO_639_2_code)  # Output: 'pol'
  print(detected_language.ISO_639_3_code)  # Output: 'pol'
  print(detected_language.language_name)  # Output 'Polish'

# Translate text
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "en")
print(translated_text)  # Output: "Hello how are you? My name is Adam"
