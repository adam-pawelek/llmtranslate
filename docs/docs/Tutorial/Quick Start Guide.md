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
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

```

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


### Language Detection

To detect the language of a given text:

```python
from llmtranslate import TranslatorOpenAI

# Set your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

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

To translate text containing multiple languages into another language:

```python
from llmtranslate import TranslatorOpenAI

# Set your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

# Translate text
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "en")
print(translated_text)  # Output: "Hello how are you? My name is Adam"
```


### Full Example

Here is a complete example demonstrating how to use the library:

```python
from llmtranslate import TranslatorOpenAI

# Initialize the translator with your OpenAI API key
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY")

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

```