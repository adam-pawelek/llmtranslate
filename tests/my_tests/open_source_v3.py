import os
from llmtranslate import TranslatorOpenSource

translator = TranslatorOpenSource(
    api_key=os.environ.get("YOUR_HF_TOKEN"),
    llm_endpoint="https://api-inference.huggingface.co/models/microsoft/Phi-3.5-mini-instruct/v1",
    model="meta-llama/Llama-3.2-1B-Instruct"
)

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