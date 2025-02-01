import asyncio
import os
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from llmtranslate import AsyncTranslator, Translator, get_language_info


class TranslationAccuracy(BaseModel):
    is_this_translation_accurate: bool

async def check_if_translation_is_accurate(
        chat_model_to_check_translation: BaseChatModel,
        translator: AsyncTranslator,
        text_to_translate: str,
        source_lang: str,
        translate_to_lang: str,
        expected_translation: str
    ):
    translated_text = await translator.translate(text_to_translate,translate_to_lang)
    prompt_template = f"""
    Compare the following two texts to determine if the translation is accurate:

    Translated Text: "{translated_text}"

    Expected Text: "{expected_translation}"

    If the texts convey the same meaning and include the important parts of the sentence, respond with "true". 
    If the translation omits any key parts of the sentence or alters the meaning in a significant way, respond with "false". Minor word changes are acceptable as long as they do not affect the overall meaning, but be careful about omissions or changes that could lead to a different understanding of the text.
    """

    system_prompt = """You are an assistant that compares two texts for translation accuracy. 
    You will analyze the 'Translated Text' and the 'Expected Text' provided by the user and determine if they convey the same meaning and include all key parts. 
    Be cautious of omissions or changes that might lead to a different understanding, but allow minor word changes if they do not impact the overall meaning.
    You should answer in json format. You can answer only by providing "true" or "false"  in json format.
    Here is format that you should answer.
    {{
        "is_this_translation_accurate": "true"
    }}
    """

    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", prompt_template)])
    structured_llm = chat_model_to_check_translation.with_structured_output(TranslationAccuracy)
    few_shot_structured_llm = prompt | structured_llm
    response = await few_shot_structured_llm.ainvoke({"":""})
    language_info = get_language_info(source_lang)
    result = {
        "supported_language": response.is_this_translation_accurate,
        "language_name": language_info["language_name"],
        "ISO_639_1_code": language_info["ISO_639_1_code"],
    }
    return result



llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=os.getenv("OPENAI_API_KEY"))
translator = AsyncTranslator(llm=llm, max_translation_chunk_length=100, max_translation_chunk_length_multilang=100)


async def benchmark_one_text(
        translator: AsyncTranslator,
        chat_model_to_check_translation: BaseChatModel,
        sentences_in_different_languages: dict[str: str],
        translate_to_lang: str,
        expected_translation: str
    ):

    tasks = []
    for source_lang, sentence_in_different_language in sentences_in_different_languages.items():
        tasks.append( check_if_translation_is_accurate(
            chat_model_to_check_translation=chat_model_to_check_translation,
            translator=translator,
            text_to_translate=sentence_in_different_language,
            source_lang=source_lang,
            translate_to_lang=translate_to_lang,
            expected_translation=expected_translation
        ))


    moj = await asyncio.gather(*tasks)
    return moj




print(asyncio.run(benchmark_one_text(
    translator= translator,
    chat_model_to_check_translation=llm,
    sentences_in_different_languages={"pl": "Czesc jak sie masz?"},
    translate_to_lang="English",
    expected_translation="Hi how are you? my name is Adam"
)))




