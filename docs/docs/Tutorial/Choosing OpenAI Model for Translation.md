## Choosing OpenAI Model for Translation

When using the `TranslatorOpenAI` class for translation tasks, you have two options to specify the model:

1. Provide the model name as a string.
2. Use the `ModelForTranslator` enum to select from predefined models.

### Option 1: Using Model Name as a String

You can directly pass the model name as a string when creating an instance of `TranslatorOpenAI`.

```python
from llmtranslate import TranslatorOpenAI

# Example with a model name as a string
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY", "gpt-4o-mini")
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "eng")
print(translated_text)
```

### Option 2: Using the `ModelForTranslator` Enum

Alternatively, you can use the `ModelForTranslator` enum to select a model. This enum contains predefined models that have been tested and come with specific versions.

```python
from llmtranslate import TranslatorOpenAI
from llmtranslate import ModelForTranslator

# Example using the ModelForTranslator enum
translator = TranslatorOpenAI(open_ai_api_key="YOUR_OPENAI_API_KEY", ModelForTranslator.GPT_4o_mini)
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "eng")
print(translated_text)
```

### Available Models in `ModelForTranslator` Enum

```python
from enum import Enum

class ModelForTranslator(Enum):
    BEST_BIG_MODEL = "gpt-4o-2024-08-06"
    BEST_SMALL_MODEL = "gpt-4o-mini"
    GPT_4o = "gpt-4o-2024-08-06"
    GPT_4o_mini = "gpt-4o-mini"
```

- **BEST_BIG_MODEL**: `"gpt-4o-2024-08-06"` - Represents the best large model available.
- **BEST_SMALL_MODEL**: `"gpt-4o-mini"` - Represents the best smaller model, optimized for speed.
- **GPT_4o**: `"gpt-4o-2024-08-06"` - Specific version of GPT-4o.
- **GPT_4o_mini**: `"gpt-4o-mini"` - A smaller version of GPT-4o.

### Summary

- **Flexibility**: Choose between using a string or the enum based on your preference.
- **Predefined Models**: The `ModelForTranslator` enum provides a convenient way to select tested models with known performance characteristics.


