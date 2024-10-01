
# TranslatorMistralCloud Class Documentation

The `TranslatorMistralCloud` class is fully compatible with both `TranslatorOpenSourceLLM` and `TranslatorOpenAI` classes. It contains all their methods and uses models hosted on the Mistral cloud for translation, language detection, and other tasks, providing the same functionality with cloud-based execution.


## How to Use

### Initialization

To use the `TranslatorMistralCloud` class, initialize it with your Mistral API key. Optionally, you can specify a model, with `MISTRAL_LARGE` as the default.

```python
from llmtranslate import TranslatorMistralCloud, ModelForTranslator

# Initialize with API key
translator = TranslatorMistralCloud(open_ai_api_key="your_mistral_api_key")
```

### Choose Mistral model 
The `TranslatorMistralCloud` class allows you to choose a translation model when initializing. By default, it uses `MISTRAL_LARGE`, but you can specify other models using the `ModelForTranslator` enum or as a string.

**Example using Enum:**
```python
from my_translation_module import TranslatorMistralCloud, ModelForTranslator

translator = TranslatorMistralCloud(open_ai_api_key="your_api_key_here", chatgpt_model_name=ModelForTranslator.MISTRAL_NEMO)
```

**Example using String**
```python
from my_translation_module import TranslatorMistralCloud, ModelForTranslator

translator = TranslatorMistralCloud(open_ai_api_key="your_api_key_here", chatgpt_model_name="open-mistral-nemo")

```




### Translate


Translates the provided text into the specified language using the ISO 639-1 code.

- **Parameters:**
  - `text`: The text to translate.
  - `to_language`: Target language (default is English: `"eng"`).
  

```python
from llmtranslate import TranslatorMistralCloud
translator = TranslatorMistralCloud(open_ai_api_key="your_mistral_api_key")
translated_text = translator.translate("Bonjour", "en")
print(translated_text)  # Output: Hello
```

### Detect language

Detects the language of the given text and returns its ISO 639-1 code.


```python
from llmtranslate import TranslatorMistralCloud
translator = TranslatorMistralCloud(open_ai_api_key="your_mistral_api_key")
detected_language = translator.get_text_language("jak ty się nazywasz")
if detected_language is not None:
    print(detected_language.ISO_639_1_code)  # Output: 'pl'
    print(detected_language.ISO_639_2_code)  # Output: 'pol'
    print(detected_language.ISO_639_3_code)  # Output: 'pol'
    print(detected_language.language_name)  # Output 'Polish'
```

!!! warning
    If the translator does not detect any language, it will return None.<br>
    Before using results of translator detection you should check if it returned correct result or None



## Example Usage

```python
from llmtranslate import TranslatorMistralCloud
translator = TranslatorMistralCloud("your_mistral_api_key")

# Translate text to English
translated_text = translator.translate("こんにちは", "en")
print(translated_text)  # Output: Hello

# Detect language
detected_language = translator.get_text_language("jak ty się nazywasz")
if detected_language is not None:
    print(detected_language.ISO_639_1_code)  # Output: 'pl'
    print(detected_language.ISO_639_2_code)  # Output: 'pol'
    print(detected_language.ISO_639_3_code)  # Output: 'pol'
    print(detected_language.language_name)  # Output 'Polish'

```
