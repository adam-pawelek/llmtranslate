from typing import List
from pydantic import BaseModel
from llmtranslate.utils.available_languages import get_language_info



gpt_4o_supported_languages = [
    {"ISO_639_1_code": "en", "translation_quality": "high"},
    {"ISO_639_1_code": "zh", "translation_quality": "high"},
    {"ISO_639_1_code": "hi", "translation_quality": "high"},
    {"ISO_639_1_code": "es", "translation_quality": "high"},
    {"ISO_639_1_code": "fr", "translation_quality": "high"},
    {"ISO_639_1_code": "de", "translation_quality": "high"},
    {"ISO_639_1_code": "ru", "translation_quality": "high"},
    {"ISO_639_1_code": "ar", "translation_quality": "high"},
    {"ISO_639_1_code": "it", "translation_quality": "high"},
    {"ISO_639_1_code": "ko", "translation_quality": "high"},
    {"ISO_639_1_code": "pa", "translation_quality": "medium"},
    {"ISO_639_1_code": "bn", "translation_quality": "high"},
    {"ISO_639_1_code": "pt", "translation_quality": "high"},
    {"ISO_639_1_code": "id", "translation_quality": "high"},
    {"ISO_639_1_code": "ur", "translation_quality": "medium"},
    {"ISO_639_1_code": "pt", "translation_quality": "high"},
    {"ISO_639_1_code": "fa", "translation_quality": "high"},
    {"ISO_639_1_code": "vi", "translation_quality": "high"},
    {"ISO_639_1_code": "pl", "translation_quality": "high"},
    {"ISO_639_1_code": "sm", "translation_quality": "medium"},
    {"ISO_639_1_code": "th", "translation_quality": "high"},
    {"ISO_639_1_code": "uk", "translation_quality": "high"},
    {"ISO_639_1_code": "tr", "translation_quality": "high"},
    {"ISO_639_1_code": "mi", "translation_quality": "medium"},
    {"ISO_639_1_code": "no", "translation_quality": "high"},
    {"ISO_639_1_code": "nl", "translation_quality": "high"},
    {"ISO_639_1_code": "el", "translation_quality": "high"},
    {"ISO_639_1_code": "ro", "translation_quality": "high"},
    {"ISO_639_1_code": "sw", "translation_quality": "high"},
    {"ISO_639_1_code": "hu", "translation_quality": "high"},
    {"ISO_639_1_code": "he", "translation_quality": "high"},
    {"ISO_639_1_code": "sv", "translation_quality": "high"},
    {"ISO_639_1_code": "cs", "translation_quality": "high"},
    {"ISO_639_1_code": "fi", "translation_quality": "high"},
    {"ISO_639_1_code": "am", "translation_quality": "medium"},
    {"ISO_639_1_code": "tl", "translation_quality": "high"},
    {"ISO_639_1_code": "my", "translation_quality": "medium"},
    {"ISO_639_1_code": "ta", "translation_quality": "high"},
    {"ISO_639_1_code": "kn", "translation_quality": "high"},
    {"ISO_639_1_code": "ps", "translation_quality": "medium"},
    {"ISO_639_1_code": "yo", "translation_quality": "medium"},
    {"ISO_639_1_code": "ms", "translation_quality": "high"},
    {"ISO_639_1_code": "ht", "translation_quality": "medium"},
    {"ISO_639_1_code": "ne", "translation_quality": "medium"},
    {"ISO_639_1_code": "si", "translation_quality": "medium"},
    {"ISO_639_1_code": "ca", "translation_quality": "high"},
    {"ISO_639_1_code": "mg", "translation_quality": "medium"},
    {"ISO_639_1_code": "lv", "translation_quality": "high"},
    {"ISO_639_1_code": "lt", "translation_quality": "high"},
    {"ISO_639_1_code": "et", "translation_quality": "high"},
    {"ISO_639_1_code": "so", "translation_quality": "medium"},
    {"ISO_639_1_code": "ti", "translation_quality": "medium"},
    {"ISO_639_1_code": "br", "translation_quality": "medium"},
    {"ISO_639_1_code": "fj", "translation_quality": "medium"},
    {"ISO_639_1_code": "mt", "translation_quality": "high"},
    {"ISO_639_1_code": "co", "translation_quality": "medium"},
    {"ISO_639_1_code": "lb", "translation_quality": "medium"},
    {"ISO_639_1_code": "oc", "translation_quality": "medium"},
    {"ISO_639_1_code": "cy", "translation_quality": "high"},
    {"ISO_639_1_code": "sq", "translation_quality": "high"},
    {"ISO_639_1_code": "mk", "translation_quality": "medium"},
    {"ISO_639_1_code": "is", "translation_quality": "high"},
    {"ISO_639_1_code": "sl", "translation_quality": "high"},
    {"ISO_639_1_code": "gl", "translation_quality": "high"},
    {"ISO_639_1_code": "eu", "translation_quality": "high"},
    {"ISO_639_1_code": "az", "translation_quality": "medium"},
    {"ISO_639_1_code": "uz", "translation_quality": "medium"},
    {"ISO_639_1_code": "kk", "translation_quality": "medium"},
    {"ISO_639_1_code": "mn", "translation_quality": "medium"},
    {"ISO_639_1_code": "bo", "translation_quality": "medium"},
    {"ISO_639_1_code": "km", "translation_quality": "medium"},
    {"ISO_639_1_code": "lo", "translation_quality": "medium"},
    {"ISO_639_1_code": "km", "translation_quality": "medium"},
    {"ISO_639_1_code": "te", "translation_quality": "high"},
    {"ISO_639_1_code": "mr", "translation_quality": "high"},
    {"ISO_639_1_code": "ny", "translation_quality": "medium"},
    {"ISO_639_1_code": "eo", "translation_quality": "medium"},
    {"ISO_639_1_code": "ku", "translation_quality": "medium"},
    {"ISO_639_1_code": "tg", "translation_quality": "medium"},
    {"ISO_639_1_code": "xh", "translation_quality": "medium"},
    {"ISO_639_1_code": "yi", "translation_quality": "medium"},
    {"ISO_639_1_code": "zu", "translation_quality": "medium"},
    {"ISO_639_1_code": "su", "translation_quality": "medium"},
    {"ISO_639_1_code": "tt", "translation_quality": "medium"},
    {"ISO_639_1_code": "qu", "translation_quality": "medium"},
    {"ISO_639_1_code": "ug", "translation_quality": "medium"},
    {"ISO_639_1_code": "wo", "translation_quality": "medium"},
    {"ISO_639_1_code": "tn", "translation_quality": "medium"}
]





class SupportedLanguage(BaseModel):
    ISO_639_1_code: str
    ISO_639_2_code: str
    ISO_639_3_code: str
    language_name: str
    translation_quality: str



class SupportedLanguages(BaseModel):
    ISO_639_1_codes: List[str]
    iso_639_2_codes: List[str]
    iso_639_3_codes: List[str]
    language_names: List[str]
    languages_full_data: List[SupportedLanguage]


class SupportedLanguagesBasedOnQuality(BaseModel):
    languages: SupportedLanguages
    high_quality_translation_languages: SupportedLanguages
    high_medium_quality_translation_languages: SupportedLanguages
    low_quality_translation_languages: SupportedLanguages
    medium_quality_translation_languages: SupportedLanguages


def create_language_list_based_on_translation_quality(list_of_languages_dicts, translation_quality: list) -> SupportedLanguages:
    filtered_list = []

    for language_dict in list_of_languages_dicts:
        if language_dict["translation_quality"] in translation_quality:
            language_data = get_language_info(language_dict["ISO_639_1_code"])
            filtered_list.append({
                "ISO_639_1_code": language_data["ISO_639_1_code"],
                "ISO_639_2_code": language_data["ISO_639_2_code"],
                "ISO_639_3_code": language_data["ISO_639_3_code"],
                "language_name": language_data["language_name"],
                "translation_quality": language_dict["translation_quality"],
            })

    ISO_639_1_codes = [language_dict['ISO_639_1_code'] for language_dict in filtered_list]
    iso_639_2_codes = [language_dict['ISO_639_2_code'] for language_dict in filtered_list]
    iso_639_3_codes = [language_dict['ISO_639_3_code'] for language_dict in filtered_list]
    language_names  = [language_dict['language_name'] for language_dict in filtered_list]
    languages_full_data = [SupportedLanguage(**language_dict) for language_dict in filtered_list]

    return SupportedLanguages(
        ISO_639_1_codes=ISO_639_1_codes,
        iso_639_2_codes=iso_639_2_codes,
        iso_639_3_codes=iso_639_3_codes,
        language_names=language_names,
        languages_full_data=languages_full_data)





def create_supported_languages_based_on_quality(list_of_languages_dicts) -> SupportedLanguagesBasedOnQuality:

    languages = create_language_list_based_on_translation_quality(list_of_languages_dicts, ["high", "medium", "low"])
    high_quality_translation_languages = create_language_list_based_on_translation_quality(list_of_languages_dicts, ["high"])
    high_medium_quality_translation_languages = create_language_list_based_on_translation_quality(list_of_languages_dicts, ["high", "medium"])
    medium_quality_translation_languages = create_language_list_based_on_translation_quality(list_of_languages_dicts, ["medium"])
    low_quality_translation_languages = create_language_list_based_on_translation_quality(list_of_languages_dicts, ["low"])

    return SupportedLanguagesBasedOnQuality(languages=languages,
                                            high_quality_translation_languages=high_quality_translation_languages,
                                            high_medium_quality_translation_languages=high_medium_quality_translation_languages,
                                            low_quality_translation_languages=low_quality_translation_languages,
                                            medium_quality_translation_languages=medium_quality_translation_languages)



