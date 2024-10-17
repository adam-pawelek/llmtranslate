# llmtranslate
[![Test](https://github.com/adam-pawelek/llmtranslate/actions/workflows/test.yml/badge.svg)](https://github.com/adam-pawelek/llmtranslate/actions/workflows/test.yml)
[![Python package - Publish](https://github.com/adam-pawelek/llmtranslate/actions/workflows/publish.yml/badge.svg)](https://github.com/adam-pawelek/llmtranslate/actions/workflows/publish.yml)
[![Docs](https://img.shields.io/badge/docs-llmtranslate-brightgreen)](https://llm-translate.com/)
[![PyPI version](https://img.shields.io/pypi/v/llmtranslate?color=brightgreen)](https://pypi.org/project/llmtranslate/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/adam-pawelek/llmtranslate?tab=MIT-1-ov-file)
[![codecov](https://codecov.io/github/adam-pawelek/llmtranslate/graph/badge.svg?token=WCQOJC032S)](https://codecov.io/github/adam-pawelek/llmtranslate)
[![Downloads](https://static.pepy.tech/badge/llmtranslate)](https://pepy.tech/project/llmtranslate)

## Overview

llmtranslate is a Python library designed to identify the language of a given text and translate text between multiple languages using OpenAI's GPT-4o. The library is especially useful for translating text containing multiple languages into a single target language.

## Features

- **Language Detection:** Identify the language of a given text in ISO 639-1 format.
- **Translation:** Translate text containing multiple languages into another language in ISO 639-1 format.

## Documentation
Comprehensive documentation, including detailed usage information, is available at https://llm-translate.com

## Requirements

To use this library, you must have an OpenAI API key. This key allows the library to utilize OpenAI's GPT-4o for translation and language detection.



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

> [!IMPORTANT]
> If the translator does not detect any language, it will return None.<br>
> Before using results of translator detection you should check if it returned correct result or None

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



### Setting the Azure OpenAI API Key

If you are using Azure's OpenAI services, you need to set your Azure OpenAI API key along with additional required parameters. Use the TranslatorAzureOpenAI class for this.

```python
from llmtranslate import TranslatorAzureOpenAI

# Set your Azure OpenAI API key and related parameters
translator = TranslatorAzureOpenAI(
  azure_endpoint="YOUR_AZURE_ENDPOINT",
  api_key="YOUR_AZURE_API_KEY",
  api_version="YOUR_API_VERSION",
  azure_deployment="YOUR_AZURE_DEPLOYMENT"
)

```



## Supported Languages

llmtranslate supports all languages supported by GPT-4o. For a complete list of language codes, you can visit the [ISO 639-1 website](https://localizely.com/iso-639-1-list/).

Here is a table showing which languages are supported by gpt-4o and gpt4o-mini:

| Language Name     | Language Code | Supported by gpt-4o | Supported by gpt4o-mini |
|-------------------|---------------|---------------------|-------------------------|
| English           | en            | Yes                 | Yes                     |
| Mandarin Chinese  | zh            | Yes                 | Yes                     |
| Hindi             | hi            | Yes                 | Yes                     |
| Spanish           | es            | Yes                 | Yes                     |
| French            | fr            | Yes                 | Yes                     |
| German            | de            | Yes                 | Yes                     |
| Russian           | ru            | Yes                 | Yes                     |
| Arabic            | ar            | Yes                 | Yes                     |
| Italian           | it            | Yes                 | Yes                     |
| Korean            | ko            | Yes                 | Yes                     |
| Punjabi           | pa            | Yes                 | Yes                     |
| Bengali           | bn            | Yes                 | Yes                     |
| Portuguese        | pt            | Yes                 | Yes                     |
| Indonesian        | id            | Yes                 | Yes                     |
| Urdu              | ur            | Yes                 | Yes                     |
| Persian (Farsi)   | fa            | Yes                 | Yes                     |
| Vietnamese        | vi            | Yes                 | Yes                     |
| Polish            | pl            | Yes                 | Yes                     |
| Samoan            | sm            | Yes                 | Yes                     |
| Thai              | th            | Yes                 | Yes                     |
| Ukrainian         | uk            | Yes                 | Yes                     |
| Turkish           | tr            | Yes                 | Yes                     |
| Maori             | mi            | **No**              | **No**                  |
| Norwegian         | no            | Yes                 | Yes                     |
| Dutch             | nl            | Yes                 | Yes                     |
| Greek             | el            | Yes                 | Yes                     |
| Romanian          | ro            | Yes                 | Yes                     |
| Swahili           | sw            | Yes                 | Yes                     |
| Hungarian         | hu            | Yes                 | Yes                     |
| Hebrew            | he            | Yes                 | Yes                     |
| Swedish           | sv            | Yes                 | Yes                     |
| Czech             | cs            | Yes                 | Yes                     |
| Finnish           | fi            | Yes                 | Yes                     |
| Amharic           | am            | **No**              | **No**                  |
| Tagalog           | tl            | Yes                 | Yes                     |
| Burmese           | my            | Yes                 | Yes                     |
| Tamil             | ta            | Yes                 | Yes                     |
| Kannada           | kn            | Yes                 | Yes                     |
| Pashto            | ps            | Yes                 | Yes                     |
| Yoruba            | yo            | Yes                 | Yes                     |
| Malay             | ms            | Yes                 | Yes                     |
| Haitian Creole    | ht            | Yes                 | Yes                     |
| Nepali            | ne            | Yes                 | Yes                     |
| Sinhala           | si            | Yes                 | Yes                     |
| Catalan           | ca            | Yes                 | Yes                     |
| Malagasy          | mg            | Yes                 | Yes                     |
| Latvian           | lv            | Yes                 | Yes                     |
| Lithuanian        | lt            | Yes                 | Yes                     |
| Estonian          | et            | Yes                 | Yes                     |
| Somali            | so            | Yes                 | Yes                     |
| Tigrinya          | ti            | **No**              | **No**                  |
| Breton            | br            | **No**              | **No**                  |
| Fijian            | fj            | Yes                 | **No**                  |
| Maltese           | mt            | Yes                 | Yes                     |
| Corsican          | co            | Yes                 | Yes                     |
| Luxembourgish     | lb            | Yes                 | Yes                     |
| Occitan           | oc            | Yes                 | Yes                     |
| Welsh             | cy            | Yes                 | Yes                     |
| Albanian          | sq            | Yes                 | Yes                     |
| Macedonian        | mk            | Yes                 | Yes                     |
| Icelandic         | is            | Yes                 | Yes                     |
| Slovenian         | sl            | Yes                 | Yes                     |
| Galician          | gl            | Yes                 | Yes                     |
| Basque            | eu            | Yes                 | Yes                     |
| Azerbaijani       | az            | Yes                 | Yes                     |
| Uzbek             | uz            | Yes                 | Yes                     |
| Kazakh            | kk            | Yes                 | Yes                     |
| Mongolian         | mn            | Yes                 | Yes                     |
| Tibetan           | bo            | **No**              | **No**                  |
| Khmer             | km            | Yes                 | **No**                  |
| Lao               | lo            | Yes                 | Yes                     |
| Telugu            | te            | Yes                 | Yes                     |
| Marathi           | mr            | Yes                 | Yes                     |
| Chichewa          | ny            | Yes                 | Yes                     |
| Esperanto         | eo            | Yes                 | Yes                     |
| Kurdish           | ku            | **No**              | **No**                  |
| Tajik             | tg            | Yes                 | Yes                     |
| Xhosa             | xh            | Yes                 | **No**                  |
| Yiddish           | yi            | Yes                 | Yes                     |
| Zulu              | zu            | Yes                 | Yes                     |
| Sundanese         | su            | Yes                 | Yes                     |
| Tatar             | tt            | Yes                 | Yes                     |
| Quechua           | qu            | **No**              | **No**                  |
| Uighur            | ug            | **No**              | **No**                  |
| Wolof             | wo            | **No**              | **No**                  |
| Tswana            | tn            | Yes                 | Yes                     |


## Additional Resources

- [PyPI page](https://pypi.org/project/llmtranslate/)
- [ISO 639-1 Codes](https://localizely.com/iso-639-1-list/)
- [Github project repository](https://github.com/adam-pawelek/llmtranslate)
- [Documentation](https://llm-translate.com/)

## Authors
- Adam Pawełek  
  - [LinkedIn](https://www.linkedin.com/in/adam-roman-pawelek/)  
  - [Email](mailto:adam.pwk@outlook.com)
  


## License

llmtranslate is licensed under the MIT License. See the LICENSE file for more details.


