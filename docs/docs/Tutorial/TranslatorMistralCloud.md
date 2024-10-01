
# TranslatorMistralCloud Class Documentation

The `TranslatorMistralCloud` class contains all the methods provided by the `TranslatorOpenSourceLLM` and `TranslatorOpenAI`. It leverages models hosted on the Mistral cloud to perform tasks such as text translation, language detection.

This class serves as a cloud-based alternative, utilizing Mistral’s models for all its operations, ensuring that the same functionality as `TranslatorOpenSourceLLM` is available while relying on Mistral’s cloud infrastructure for execution.


## How to Use

### Initialization

To use the `TranslatorMistralCloud` class, initialize it with your Mistral API key. Optionally, you can specify a model, with `MISTRAL_LARGE` as the default.

```python
from llmtranslate import TranslatorMistralCloud, ModelForTranslator

# Initialize with API key
translator = TranslatorMistralCloud(open_ai_api_key="your_api_key_here")
```

### Methods

#### `translate(text: str, to_language: str = "eng") -> str`

Translates the provided text into the specified language using the ISO 639-1 code.

- **Parameters:**
  - `text`: The text to translate.
  - `to_language`: Target language (default is English: `"eng"`).
  
- **Example:**
```python
from llmtranslate import TranslatorMistralCloud
translator = TranslatorMistralCloud(open_ai_api_key="your_api_key_here")
translated_text = translator.translate("Bonjour", "eng")
print(translated_text)  # Output: Hello
```

#### `get_text_language(text: str) -> TextLanguage`

Detects the language of the given text and returns its ISO 639-1 code.

- **Example:**
```python
from llmtranslate import TranslatorMistralCloud
translator = TranslatorMistralCloud(open_ai_api_key="your_api_key_here")
language_info = translator.get_text_language("Hola")
print (language_info.ISO_639_1_code)  # Output: "es"
```


## Example Usage

```python
from llmtranslate import TranslatorMistralCloud
translator = TranslatorMistralCloud("your_api_key")

# Translate text to English
translated_text = translator.translate("こんにちは", "eng")
print(translated_text)  # Output: Hello

# Detect language
detected_language = translator.get_text_language("Merci")
print(detected_language.language_name)  # Output: French

# Count languages in text
num_languages = translator.how_many_languages_are_in_text("Merci, Thank you")
print(num_languages)  # Output: 2
```
