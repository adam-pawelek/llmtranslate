import json
import os

from openai import OpenAI
from pydantic import BaseModel

from llmtranslate import TranslatorOpenAI, ModelForTranslator, TranslatorMistralCloud, get_language_info, Translator
from llmtranslate.benchmark.data.short_text_data import test_data_large_learning_new_language




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
        model="gpt-4o",
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


def check_translation_to_language_using_chatgpt(translator, language_to_translate, language_to_check, open_ai_api_key):
    if "not available" in language_to_translate:
        print(language_to_translate)
        return False

    translator_open_ai = TranslatorOpenAI(api_key=open_ai_api_key)
    translation_to_compare = translator_open_ai.translate(language_to_translate, language_to_check)


    translated_text = translator.translate(language_to_translate, language_to_check)
    print("hallo to jest tekst")
    print(translated_text)

    return check_if_translation_is_accurate(translated_text, translation_to_compare)



#translator_to_test = TranslatorOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o")
translator_to_test = translator = TranslatorMistralCloud(os.environ.get("MISTRAL_API_KEY"), ModelForTranslator.MISTRAL_NEMO.value)
#print(check_translation_to_language_using_chatgpt(translator_to_test,test_data_large_learning_new_language[6][0] , "gv", os.getenv("OPENAI_API_KEY")))




def benchmark_translation_to_language_using_chatgpt(translator, language_list_to_translate, language_to_check, open_ai_api_key):
    result = []
    for text_to_translate, language_code in language_list_to_translate:
        supported_language = check_translation_to_language_using_chatgpt(
            translator,
            text_to_translate,
            language_to_check,
            open_ai_api_key#os.getenv("OPENAI_API_KEY")
        )
        language_info = get_language_info(language_code)
        result.append({
            "supported_language": supported_language,
            "language_name": language_info["language_name"],
            "ISO_639_1_code": language_info["ISO_639_1_code"],
        })

    return result


def check_translation_to_language_using_original_text_in_language_to_check(translator, language_to_translate, language_to_check, open_ai_api_key, original_text_in_language_to_check):
    if "not available" in language_to_translate:
        print(language_to_translate)
        return False

    translated_text = translator.translate(language_to_translate, language_to_check)
    print("hallo to jest tekst")
    print(translated_text)

    return check_if_translation_is_accurate(translated_text, original_text_in_language_to_check)


def benchmark_text_recognition(translator: Translator, language_list_to_translate):
    result = []
    for text_to_recognize, language_code in language_list_to_translate:
        language_code_from_translator = translator.get_text_language(text_to_recognize)
        language_info = get_language_info(language_code)
        dict_to_append = {
            "language_name": language_info["language_name"],
            "ISO_639_1_code": language_info["ISO_639_1_code"]
        }
        if language_code_from_translator == None:
            dict_to_append["supported_language"] = False

        elif language_code_from_translator.ISO_639_1_code == language_code:
            dict_to_append["supported_language"] = True
        else:
            dict_to_append["supported_language"] = False

        result.append(dict_to_append)

    return result




#moj = benchmark_text_recognition(translator_to_test,test_data_large_learning_new_language[0:10])


moj = benchmark_translation_to_language_using_chatgpt(translator_to_test,test_data_large_learning_new_language[0:10], "en", os.getenv("OPENAI_API_KEY"))

json_string = json.dumps(moj, indent=4)
print(json_string)
