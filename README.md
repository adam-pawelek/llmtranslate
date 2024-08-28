# llm-translate
[![Test](https://github.com/adam-pawelek/llm-translate/actions/workflows/test.yml/badge.svg)](https://github.com/adam-pawelek/llm-translate/actions/workflows/test.yml)
[![Python package - Publish](https://github.com/adam-pawelek/llm-translate/actions/workflows/publish.yml/badge.svg)](https://github.com/adam-pawelek/llm-translate/actions/workflows/publish.yml)
[![Python Versions](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue)](https://www.python.org/)
[![PyPI version](https://img.shields.io/pypi/v/llm_translate)](https://pypi.org/project/llm_translate/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/github/adam-pawelek/llm-translate/graph/badge.svg?token=WCQOJC032S)](https://codecov.io/github/adam-pawelek/llm-translate)
## Overview

llm-translate is a Python library designed to identify the language of a given text and translate text between multiple languages using OpenAI's GPT-4o. The library is especially useful for translating text containing multiple languages into a single target language.

## Features

- **Language Detection:** Identify the language of a given text in ISO 639-1 format.
- **Translation:** Translate text containing multiple languages into another language in ISO 639-1 format.

## Requirements

To use this library, you must have an OpenAI API key. This key allows the library to utilize OpenAI's GPT-4o for translation and language detection.



## Installation

You can install the llm-translate library from PyPI:

```bash
pip install llm-translate
```

## Usage

### Setting the OpenAI API Key

Before using llm-translate with OpenAI, you need to set your OpenAI API key. You can do this by creating an instance of the TranslatorOpenAI class.
```python
from llm_translate.translator import TranslatorOpenAI

# Set your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

```

### Setting the Azure OpenAI API Key

If you are using Azure's OpenAI services, you need to set your Azure OpenAI API key along with additional required parameters. Use the TranslatorAzureOpenAI class for this.
```python
from llm_translate.translator import TranslatorAzureOpenAI

# Set your Azure OpenAI API key and related parameters
translator = TranslatorAzureOpenAI(
    azure_endpoint="YOUR_AZURE_ENDPOINT",
    api_key="YOUR_AZURE_API_KEY",
    api_version="YOUR_API_VERSION",
    azure_deployment="YOUR_AZURE_DEPLOYMENT"
)

```


### Language Detection

To detect the language of a given text:

```python
from llm_translate.translator import TranslatorOpenAI
# Set your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

# Detect language
detected_language = translator.get_text_language("Hello world")
print(detected_language.language_ISO_639_1_code)  # Output: 'en'
print(detected_language.language_name)  # Output: 'English'

```

> [!IMPORTANT]
> If the translator does not detect any language, it will return "" for every detected_language value: <br>
> detected_language.language_ISO_639_1_code -> "" <br>
> detected_language.language_name -> ""

### Translation

To translate text containing multiple languages into another language:

```python
from llm_translate.translator import TranslatorOpenAI
# Set your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

# Translate text
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "en")
print(translated_text)  # Output: "Hello how are you? My name is Adam"
```


### Full Example

Here is a complete example demonstrating how to use the library:

```python
from llm_translate.translator import TranslatorOpenAI

# Initialize the translator with your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

# Detect language
detected_language = translator.get_text_language("jak ty się nazywasz")
print(detected_language.language_ISO_639_1_code)  # Output: 'pl'
print(detected_language.language_name) # Output 'Polish'

# Translate text
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "en")
print(translated_text)  # Output: "Hello how are you? My name is Adam"

```

## Supported Languages

llm-translate supports all languages supported by GPT-4o. For a complete list of language codes, you can visit the [ISO 639-1 website](https://localizely.com/iso-639-1-list/).

Here are some of the most popular languages and their ISO 639-1 codes:

- **English**: `en`
- **Spanish**: `es`
- **French**: `fr`
- **German**: `de`
- **Chinese**: `zh`
- **Japanese**: `ja`
- **Korean**: `ko`
- **Portuguese**: `pt`
- **Russian**: `ru`
- **Italian**: `it`
- **Dutch**: `nl`
- **Arabic**: `ar`
- **Hindi**: `hi`
- **Bengali**: `bn`
- **Turkish**: `tr`
- **Polish**: `pl`
- **Swedish**: `sv`
- **Norwegian**: `no`
- **Danish**: `da`
- **Finnish**: `fi`
- **Greek**: `el`
- **Hebrew**: `he`

## Additional Resources

- [PyPI page](https://pypi.org/project/llm_translate/)
- [ISO 639-1 Codes](https://localizely.com/iso-639-1-list/)
- [Github project repository](https://github.com/adam-pawelek/llm-translate)

## Authors
- Adam Pawełek  
  - [LinkedIn](https://www.linkedin.com/in/adam-roman-pawelek/)  
  - [Email](mailto:adam.pwk@outlook.com)
  


## License

llm-translate is licensed under the MIT License. See the LICENSE file for more details.


