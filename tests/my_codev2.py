import os
import llm_translate
from llm_translate.translator import TranslatorOpenAI
#from llm_translate.translator import how_many_languages_are_in_text
from llm_translate.utils.enums import ModelForTranslator
from llm_translate import translator

text = """
Litwo! Ojczyzno moja! ty jesteś jak zdrowie:
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie. 
Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki, pod Twoją opiekę
Ofiarowany, martwą podniosłem powiekę;
I zaraz mogłem pieszo, do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono. 
Tymczasem przenoś moją duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą. 
Śród takich pól przed laty, nad brzegiem ruczaju
Hi how are you?
Zobaczymy czy teraz sobie z tym poradzisz
"""
#print(os.environ.get("OPENAI_API_KEY"))
translator = TranslatorOpenAI(os.environ.get("OPENAI_API_KEY"))
#llm_translate.translator.set_chatgpt_model(ChatGPTModelForTranslator.GPT_4o_mini)
print(len(text))

print()

#print(how_many_languages_are_in_text(text))
print(translator.get_text_language("jak ty się nazywasz").language_name)

detected_language = translator.get_text_language("jak ty się nazywasz")
if detected_language is not None:
    print(detected_language.ISO_639_3_code)
print(translator.get_text_language("jak ty się nazywasz").ISO_639_1_code)
print(translator.get_text_language(text))

print(translator.translate(text, "eng"))

print(translator.get_text_language("Hi how are you").ISO_639_1_code)

