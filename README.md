# llmtranslate
[![Test](https://github.com/adam-pawelek/llmtranslate/actions/workflows/test.yml/badge.svg)](https://github.com/adam-pawelek/llmtranslate/actions/workflows/test.yml)
[![Python package - Publish](https://github.com/adam-pawelek/llmtranslate/actions/workflows/publish.yml/badge.svg)](https://github.com/adam-pawelek/llmtranslate/actions/workflows/publish.yml)
[![Docs](https://img.shields.io/badge/docs-llmtranslate-brightgreen)](https://llm-translate.com/)
[![PyPI version](https://img.shields.io/pypi/v/llmtranslate?color=brightgreen)](https://pypi.org/project/llmtranslate/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/adam-pawelek/llmtranslate?tab=MIT-1-ov-file)
[![codecov](https://codecov.io/github/adam-pawelek/llmtranslate/graph/badge.svg?token=WCQOJC032S)](https://codecov.io/github/adam-pawelek/llmtranslate)
[![Downloads](https://static.pepy.tech/badge/llmtranslate)](https://pepy.tech/project/llmtranslate)


The `llmtranslate` library is a Python tool that leverages LangChain's [ChatModels](https://python.langchain.com/docs/integrations/chat/) to translate text between languages and recognize the language of a given text. This library provides both synchronous and asynchronous translators to accommodate various use cases.

---

## Installation

To ensure proper dependency management, install the required libraries in the following order:

1. Install LangChain chat libraries for your preferred LLM. For example:
   ```bash
   pip install langchain-openai
   ```

2. Install the `llmtranslate` library:
   ```bash
   pip install llmtranslate
   ```

---

## Example Using OpenAI's GPT

### Using `Translator` (Synchronous)
```python
from llmtranslate import Translator
from langchain_openai import ChatOpenAI

# Initialize the LLM and Translator
llm = ChatOpenAI(model_name="gpt-4o", openai_api_key="your_openai_api_key")
translator = Translator(llm=llm)

# Detect the language of the text
text_language = translator.get_text_language("Hi how are you?")
if text_language:
    print(text_language.ISO_639_1_code) # Output: en
    print(text_language.ISO_639_2_code) # Output: eng
    print(text_language.ISO_639_3_code) # Output: eng
    print(text_language.language_name) # Output: English

# Translate text
translated_text = translator.translate("Bonjour tout le monde", "English")
print(translated_text)  # Output: Hello everyone
```

---

### Using `AsyncTranslator` (Asynchronous)
```python
import asyncio
from llmtranslate import AsyncTranslator
from langchain_openai import ChatOpenAI

# Initialize the LLM and AsyncTranslator
llm = ChatOpenAI(model_name="gpt-4o", openai_api_key="your_openai_api_key")

async def translate_text():
    translator = AsyncTranslator(llm=llm, max_length_text_chunk_to_translate=100, max_length_text_chunk_to_translate_multiple_languages=50, max_concurrent_llm_calls=10)
    tasks = [
        translator.get_text_language("Hi how are you?"), 
        translator.translate("Hi how are you?", "Spanish")
    ]
    results = await asyncio.gather(*tasks)
    # Output the detected language information
    print(results[0])  # Output:
    # TextLanguage(
    #   Language Name: English
    #   ISO 639-1 Code: en
    #   ISO 639-2 Code: eng
    #   ISO 639-3 Code: eng
    # )
    
    # Output the translated text
    print(results[1])  # Output: Hola, ¿cómo estás?

# Run the asynchronous translation
asyncio.run(translate_text())
```

---
## Key Parameters

### `max_length_text_chunk_to_translate`
- **Description**: Defines the maximum length (in characters) of a text chunk to be translated in a single call when the text is in one language.
- **Recommendation**: If translations are not accurate, try reducing this value as weaker LLMs struggle with large chunks of text.

### `max_length_text_chunk_to_translate_multiple_languages`
- **Description**: Defines the maximum length (in characters) of a text chunk when the text contains multiple languages.
- **Recommendation**: Reduce this value for better accuracy with multi-language inputs.

### `max_concurrent_llm_calls`
- **Description**: Limits the number of concurrent calls made to the LLM.
- **Default**: 10
- **Usage**: Adjust this parameter to align with your LLM provider's concurrency limits.

---


## Other Supported LLMs Examples
You can find more examples of LangChain Chat models in the documentation at:
- [llm-translate.com](https://llm-translate.com/)
- [LangChain Documentation](https://python.langchain.com/docs/integrations/chat/)

### Anthropic's Claude
To create an instance of an Anthropic-based Chat LLM:
```bash
  pip install langchain-anthropic
  pip install llmtranslate
```
```python
from langchain_anthropic import Anthropic
from llmtranslate import Translator
llm = Anthropic(model="claude-2", anthropic_api_key="your_anthropic_api_key")
translator = Translator(llm=llm)
```

### Mistral via API
To create an instance of a Chat LLM using the Mistral API:
```bash
pip install -qU langchain_mistralai
pip install llmtranslate
```
```python
from langchain_mistral import MistralChat
from llmtranslate import Translator

llm = MistralChat(api_key="your_mistral_api_key")
translator = Translator(llm=llm)
```

---


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


