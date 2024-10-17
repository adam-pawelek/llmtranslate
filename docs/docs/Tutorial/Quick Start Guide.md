# Quick Start Guide

## Installation

You can install the llmtranslate library from PyPI:

```bash
pip install llmtranslate
```

## Usage

### Setting the OpenAI API Key

Before using llmtranslate with OpenAI, you need to set your OpenAI API key. You can do this by creating an instance of the TranslatorOpenAI class.

```python
from llmtranslate import TranslatorOpenAI

# Set your OpenAI API key
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o-mini")

```

### Language Detection

To detect the language of a given text:

```python
from llmtranslate import TranslatorOpenAI

# Set your OpenAI API key
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o-mini")

# Detect language
detected_language = translator.get_text_language("Hello world")
if detected_language is not None:
    print(detected_language.ISO_639_1_code)  # Output: 'en'
    print(detected_language.ISO_639_2_code)  # Output: 'eng'
    print(detected_language.ISO_639_3_code)  # Output: 'eng'
    print(detected_language.language_name)  # Output: 'English'

```

!!! warning
    If the translator does not detect any language, it will return None.<br>
    Before using results of translator detection you should check if it returned correct result or None

### Translation

To translate text containing multiple languages into another language, you need to provide the ISO 639 language code for the target language. For a list of all ISO 639 language codes, you can refer to this [ISO 639-1 code list website](https://localizely.com/iso-639-1-list/).

```python
from llmtranslate import TranslatorOpenAI

# Set your OpenAI API key
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o-mini")

# Translate text
translated_text = translator.translate(
    text="Cześć jak się masz? Meu nome é Adam", 
    to_language="en"  # Use ISO 639-1 code for the target language
)
print(translated_text)  # Output: "Hello how are you? My name is Adam"
```


### Full Example

Here is a complete example demonstrating how to use the library:

```python
from llmtranslate import TranslatorOpenAI

# Initialize the translator with your OpenAI API key
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o-mini")

# Detect language
detected_language = translator.get_text_language("jak ty się nazywasz")
if detected_language is not None:
    print(detected_language.ISO_639_1_code)  # Output: 'pl'
    print(detected_language.ISO_639_2_code)  # Output: 'pol'
    print(detected_language.ISO_639_3_code)  # Output: 'pol'
    print(detected_language.language_name)  # Output 'Polish'

# Translate text
translated_text = translator.translate(
    text="Cześć jak się masz? Meu nome é Adam", 
    to_language="en"
)
print(translated_text)  # Output: "Hello how are you? My name is Adam"

```

### Available OpenAI Models for Translation
The llmtranslate library provides access to various OpenAI models for translation. Below are the supported models and their use cases:

```python
from llmtranslate import TranslatorOpenAI

# Recommended for precise translation, high-precision model
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o")

# A budget-friendly option, balancing cost and quality
translator = TranslatorOpenAI(api_key="YOUR_OPENAI_API_KEY", model="gpt-4o-mini")

```


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
