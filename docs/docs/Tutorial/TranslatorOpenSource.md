# `TranslatorOpenSource` Class Documentation

The `TranslatorOpenSource` class is designed for language detection and translation using open-source large language models (LLMs) deployed on a custom endpoint. This class enables interaction with these models to detect the language of text and translate between languages.

## Initialization

```python
from llmtranslate import TranslatorOpenSource

# Create the translator object
translator = TranslatorOpenSource(api_key="YOUR_API_KEY", llm_endpoint="YOUR_LLM_ENDPOINT", model="mistralai/Mistral-Nemo-Instruct-2407")
```


The constructor initializes the `TranslatorOpenSource` class by setting up the API key, endpoint, and large language model (LLM). It also configures the maximum text length limits depending on the model.

### Parameters:

- **`api_key`**:  
   A string representing the API key that authenticates access to the LLM service. This key ensures that the service can securely connect to your model deployment.

- **`llm_endpoint`**:  
   A string representing the endpoint URL where the LLM model is deployed. This is usually a REST API endpoint provided by your deployment platform (e.g., Hugging Face or other open-source model deployment platforms).

- **`model`**:  
   A string representing the name of the model used for translation. In this case, the `mistralai/Mistral-Nemo-Instruct-2407` model is used. This model determines the capabilities and performance of the translation system.

   - For models in `MINI_MODELS`:
     - `max_length = 30`: Limits the maximum length of text chunks that can be translated in a single request.
     - `max_length_mini_text_chunk = 20`: Limits the maximum length of mini text chunks for smaller translations.
   - For larger models (those not in `MINI_MODELS`):
     - `max_length = 100`: Allows larger text chunks for translation.
     - `max_length_mini_text_chunk = 50`: Allows larger mini text chunks for more efficient translation handling.


## Example Usage

### `get_text_language()`: Detects the language of the provided text synchronously.

```python
from llmtranslate import TranslatorOpenSource

# Create the translator object
translator = TranslatorOpenSource(api_key="YOUR_API_KEY", llm_endpoint="YOUR_LLM_ENDPOINT", model="mistralai/Mistral-Nemo-Instruct-2407")

# Detect the language of a given text
detected_language = translator.get_text_language("Bonjour tout le monde")

if detected_language is not None:
    print(detected_language.ISO_639_1_code)  # Output: 'fr'
    print(detected_language.ISO_639_2_code)  # Output: 'fra'
    print(detected_language.ISO_639_3_code)  # Output: 'fra'
    print(detected_language.language_name)   # Output: 'French'
```

### `async_get_text_language()`: Detects the language of the provided text asynchronously.

```python
import asyncio
from llmtranslate import TranslatorOpenSource

# Create the translator object
translator = TranslatorOpenSource(api_key="YOUR_API_KEY", llm_endpoint="YOUR_LLM_ENDPOINT", model="mistralai/Mistral-Nemo-Instruct-2407")

# Async function to detect language
async def detect_language_async():
    detected_language = await translator.async_get_text_language("Hola, ¿cómo estás?")
    if detected_language is not None:
        print(detected_language.ISO_639_1_code)  # Output: 'es'
        print(detected_language.language_name)   # Output: 'Spanish'

# Run the async function
asyncio.run(detect_language_async())
```

### `translate()`: Translates text synchronously from one language to another.

```python
from llmtranslate import TranslatorOpenSource

# Create the translator object
translator = TranslatorOpenSource(api_key="YOUR_API_KEY", llm_endpoint="YOUR_LLM_ENDPOINT", model="mistralai/Mistral-Nemo-Instruct-2407")

# Translate text from one language to another
translated_text = translator.translate(
    text="Hallo, wie geht's?", 
    to_language="en"  # Target language in ISO 639-1 format
)
print(translated_text)  # Output: "Hello, how are you?"
```

### `async_translate_text()`: Translates text asynchronously from one language to another.

```python
import asyncio
from llmtranslate import TranslatorOpenSource

# Create the translator object
translator = TranslatorOpenSource(api_key="YOUR_API_KEY", llm_endpoint="YOUR_LLM_ENDPOINT", model="mistralai/Mistral-Nemo-Instruct-2407")

# Async function to translate text
async def translate_text_async():
    translated_text = await translator.async_translate_text(
        text="Cześć, jak się masz?", 
        to_language="en"  # Target language in ISO 639-1 format
    )
    print(translated_text)  # Output: "Hello, how are you?"

# Run the async function
asyncio.run(translate_text_async())
```
