import os
from llmtranslate import TranslatorTextGenerationInference



#print(os.environ.get("YOUR_HF_TOKEN"))
translator = TranslatorTextGenerationInference(
    api_key=os.environ.get("YOUR_HF_TOKEN"),
    #llm_endpoint="https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct/v1",
    llm_model_name="mistralai/Mistral-Small-Instruct-2409"
)

# Detect language
detected_language = translator.get_text_language("jak ty się nazywasz")
print(detected_language)
if detected_language is not None:
  print(detected_language.ISO_639_1_code)  # Output: 'pl'
  print(detected_language.ISO_639_2_code)  # Output: 'pol'
  print(detected_language.ISO_639_3_code)  # Output: 'pol'
  print(detected_language.language_name)  # Output 'Polish'



# Translate text
translated_text = translator.translate("Cześć jak się masz? Meu nome é Adam", "en")
print(translated_text)  # Output: "Hello how are you? My name is Adam"


text = """
Gospodarstwo
Powrót panicza — Spotkanie się pierwsze w pokoiku, drugie u stołu — Ważna Sędziego nauka o grzeczności — Podkomorzego uwagi polityczne nad modami — Początek sporu o Kusego i Sokoła — Żale Wojskiego — Ostatni Woźny Trybunału — Rzut oka na ówczesny stan polityczny Litwy i Europy

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



translated_text = translator.translate(text, "en")
print(translated_text)  # Output: "Hello how are you? My name is Adam"
