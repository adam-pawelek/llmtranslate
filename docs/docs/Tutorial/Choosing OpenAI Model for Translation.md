## Choosing OpenAI Model for Translation

When using the `TranslatorOpenAI` class for translation tasks, you have two options to specify the model:

1. Provide the model name as a string.
2. Use the `ModelForTranslator` enum to select from predefined models.

### Option 1: Using Model Name as a String

You can directly pass the model name as a string when creating an instance of `TranslatorOpenAI`.

```python
from llmtranslate import TranslatorOpenAI

# Example with a model name as a string
translator = TranslatorOpenAI(
    api_key="YOUR_OPENAI_API_KEY", 
    model="gpt-4o-mini"
)

translated_text = translator.translate(
    text="Cześć jak się masz? Meu nome é Adam", 
    to_language="en"
)
print(translated_text)
```

### Option 2: Using the `ModelForTranslator` Enum

Alternatively, you can use the `ModelForTranslator` enum to select a model. This enum contains predefined models that have been tested and come with specific versions.

```python
from llmtranslate import TranslatorOpenAI
from llmtranslate import ModelForTranslator

# Example using the ModelForTranslator enum
translator = TranslatorOpenAI(
    api_key="YOUR_OPENAI_API_KEY", 
    model=ModelForTranslator.GPT_4o_mini
)

translated_text = translator.translate(
    text="Cześć jak się masz? Meu nome é Adam", 
    to_language="en"
)
print(translated_text)
```

### Available Models in `ModelForTranslator` Enum

```python
from enum import Enum

class ModelForTranslator(Enum):
    BEST_BIG_MODEL = "gpt-4o"
    BEST_SMALL_MODEL = "gpt-4o-mini"
    GPT_4o = "gpt-4o"
    GPT_4o_mini = "gpt-4o-mini"
```

- **BEST_BIG_MODEL**: `"gpt-4o"` - Represents the best large model available.
- **BEST_SMALL_MODEL**: `"gpt-4o-mini"` - Represents the best smaller model, optimized for speed.
- **GPT_4o**: `"gpt-4o"` - Specific version of GPT-4o.
- **GPT_4o_mini**: `"gpt-4o-mini"` - A smaller version of GPT-4o.


## Using Asynchronous Methods

The `llmtranslate` library provides asynchronous methods to allow you to perform language detection and translation tasks efficiently in an async environment. If your application uses `asyncio` or another asynchronous framework, you can take full advantage of these async methods to avoid blocking your program while waiting for language detection or translation tasks to complete.

### Example of Using Asynchronous Methods

The following example demonstrates how to use the `async_get_text_language` and `async_translate_text` methods:

```python
import asyncio
from llmtranslate import TranslatorOpenAI

# Initialize the translator with your OpenAI API key
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o-mini")

# Async function to detect language and translate text
async def detect_and_translate():
    # Detect language asynchronously
    detected_language = await translator.async_get_text_language("Hola, ¿cómo estás?")
    if detected_language is not None:
        print(detected_language.ISO_639_1_code)  # Output: 'es'
        print(detected_language.language_name)   # Output: 'Spanish'

    # Translate text asynchronously
    translated_text = await translator.async_translate_text(
        text="Cześć jak się masz? Meu nome é Adam", 
        to_language="en"  # Use ISO 639-1 code for the target language
    )
    print(translated_text)  # Output: "Hello how are you? My name is Adam"

# Run the async function
asyncio.run(detect_and_translate())
```

### Key Asynchronous Methods

1. **`async_get_text_language(text: str)`**:
   This method detects the language of the provided text asynchronously.
   - **Parameters**: 
     - `text`: The input text whose language needs to be detected.
   - **Returns**: A `TextLanguage` object containing the detected language's ISO 639-1, ISO 639-2, ISO 639-3 codes, and the language name.
   
   **Example**:
   ```python
   detected_language = await translator.async_get_text_language("Hallo, wie geht's?")
   ```

2. **`async_translate_text(text: str, to_language: str)`**:
   This method translates the input text asynchronously to the specified target language.
   - **Parameters**:
     - `text`: The input text to be translated.
     - `to_language`: The target language in ISO 639-1 code.
   - **Returns**: A string containing the translated text.

   **Example**:
   ```python
   translated_text = await translator.async_translate_text("Bonjour tout le monde", "en")
   ```

### Why Use Asynchronous Methods?

Using asynchronous methods allows your application to handle multiple tasks concurrently, improving efficiency, especially when dealing with large amounts of text or performing multiple translations simultaneously. This non-blocking behavior is ideal for web services, APIs, and any scenario requiring high responsiveness.

### Running Asynchronous Functions

Remember that asynchronous methods must be called within an `async` function. To execute them, you can use `asyncio.run()` as shown in the examples above.



### Summary

- **Flexibility**: Choose between using a string or the enum based on your preference.
- **Predefined Models**: The `ModelForTranslator` enum provides a convenient way to select tested models with known performance characteristics.


