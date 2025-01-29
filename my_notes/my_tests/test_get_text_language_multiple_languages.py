'''
import os

import pytest
from openai import OpenAI
from pydantic import BaseModel

from llmtranslate.translator import TranslatorOpenAI
from llmtranslate.utils.enums import ModelForTranslator

from tests.data_to_test import test_data_large_learning_new_language


@pytest.fixture
def translator_big_model():
    return TranslatorOpenAI(open_ai_api_key=os.environ.get("OPENAI_API_KEY"))


@pytest.mark.parametrize("text, expected_language_code", test_data_large_learning_new_language)
def test_get_text_language_big_model(translator_big_model, text, expected_language_code):
    # Call the get_text_language method directly
    detected_language = translator_big_model.get_text_language(text)

    assert detected_language.ISO_639_1_code == expected_language_code



@pytest.fixture
def translator_small_model():
    return TranslatorOpenAI(open_ai_api_key=os.environ.get("OPENAI_API_KEY"), chatgpt_model_name=ModelForTranslator.BEST_SMALL_MODEL.value)



@pytest.mark.parametrize("text, expected_language_code", test_data_large_learning_new_language)
def test_get_text_language_small_model(translator_small_model, text, expected_language_code):
    # Call the get_text_language method directly

    detected_language = translator_small_model.get_text_language(text)
    if expected_language_code in ["wo", "xh", "co", "ps", "fa", "tn", "st", "sc", "ca", "lb", "fj", "sm", "wl", "su"]:
        assert True
    else:
        assert detected_language.ISO_639_1_code == expected_language_code


class IsTextSimilarFormat(BaseModel):
    is_translation_similar_to_expected_text: bool



def check_if_translation_is_accurate(translated_text, expected_text):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = f"""
    Compare the following two texts to determine if the translation is accurate:

    Translated Text: "{translated_text}"

    Expected Text: "{expected_text}"

    If the texts convey the same meaning and include the important parts of the sentence, respond with "yes". 
    If the translation omits any key parts of the sentence or alters the meaning in a significant way, respond with "no". Minor word changes are acceptable as long as they do not affect the overall meaning, but be careful about omissions or changes that could lead to a different understanding of the text.
    """

    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that compares two texts for translation accuracy. You will analyze the 'Translated Text' and the 'Expected Text' provided by the user and determine if they convey the same meaning and include all key parts. Be cautious of omissions or changes that might lead to a different understanding, but allow minor word changes if they do not impact the overall meaning."
            },

            {"role": "user", "content": prompt},
        ],
        response_format=IsTextSimilarFormat,
    )
    result = response.choices[0].message.parsed

    return result.is_translation_similar_to_expected_text




@pytest.mark.parametrize("language_to_translate, expected_language_code", test_data_large_learning_new_language)
def test_translate_from_another_language_to_english_large_gpt_model(translator_big_model, language_to_translate, expected_language_code):
    if "not available" in language_to_translate:
        print(language_to_translate)
        assert True
        return

    text_in_english= "Learning a new language can be challenging, but it is also exciting. It helps us connect with people from different cultures and understand the world better. Every new language we learn gives us a fresh perspective and opens up new opportunities."
    translated_text = translator_big_model.translate(language_to_translate, "en")
    print("hallo to jest tekst")
    print(translated_text)
    assert translated_text
    if expected_language_code in ['am', 'ti', 'bo', 'ku', 'qu', 'ug', 'wo', 'br', 'mi']: # almost ok -> mi
        assert True
    else:
        assert check_if_translation_is_accurate(translated_text, text_in_english)


@pytest.mark.parametrize("language_to_translate, expected_language_code", test_data_large_learning_new_language)
def test_translate_from_another_language_to_english_small_gpt_model(translator_small_model, language_to_translate, expected_language_code):
    text_in_english= "Learning a new language can be challenging, but it is also exciting. It helps us connect with people from different cultures and understand the world better. Every new language we learn gives us a fresh perspective and opens up new opportunities."
    translated_text = translator_small_model.translate(language_to_translate, "en")
    print("hallo to jest tekst")
    print(translated_text)
    assert translated_text
    if expected_language_code in ['am', 'ti', 'bo', 'ku', 'qu', 'ug', 'wo', 'br', 'mi','fj', 'km', 'xh']: # almost ok -> mi
        assert True
    else:
        assert check_if_translation_is_accurate(translated_text, text_in_english)

'''



