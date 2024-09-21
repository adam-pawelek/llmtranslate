import os
import re

from llmtranslate.translator import TranslatorOpenAI

from llmtranslate.utils.enums import ModelForTranslator

#print(os.environ.get("OPENAI_API_KEY"))

#llmtranslate.translator.set_openai_api_key(None)

translator = TranslatorOpenAI(os.environ.get("OPENAI_API_KEY"), ModelForTranslator.GPT_4o_mini.value)
print(translator.translate("Cześć jak się masz? Meu nome é Adam", "eng"))


print(translator.get_text_language("jak ty się nazywasz").language_name)
print(translator.translate("Cześć jak się masz? Meu nome é Adam", "eng"))



text_example = """
Adam Mickiewicz
Pan Tadeusz
czyli ostatni zajazd na Litwie
Księga pierwsza
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
Śród takich pól przed laty, nad brzegiem ruczaju,
Na pagórku niewielkim, we brzozowym gaju,
Stał dwór szlachecki, z drzewa, lecz podmurowany;
Świeciły się z daleka pobielane ściany,
Tym bielsze, że odbite od ciemnej zieleni
Topoli, co go bronią od wiatrów jesieni. 
Dom mieszkalny niewielki, lecz zewsząd chędogi,
I stodołę miał wielką, i przy niej trzy stogi
Użątku, co pod strzechą zmieścić się nie może.
Widać, że okolica obfita we zboże,
I widać z liczby kopic, co wzdłuż i wszerz smugów 
Świecą gęsto jak gwiazdy, widać z liczby pługów
Orzących wcześnie łany ogromne ugoru,
Czarnoziemne, zapewne należne do dworu,
Uprawne dobrze na kształt ogrodowych grządek:
Że w tym domu dostatek mieszka i porządek.
Brama na wciąż otwarta przechodniom ogłasza,
Że gościnna, i wszystkich w gościnę zaprasza. 
Właśnie dwukonną bryką wjechał młody panek
I obiegłszy dziedziniec zawrócił przed ganek.
Wysiadł z powozu; konie porzucone same,
Szczypiąc trawę ciągnęły powoli pod bramę.
We dworze pusto: bo drzwi od ganku zamknięto
Zaszczepkami i kołkiem zaszczepki przetknięto.
Podróżny do folwarku nie biegł sług zapytać,
Odemknął, wbiegł do domu, pragnął go powitać.
Dawno domu nie widział, bo w dalekim mieście
Kończył nauki, końca doczekał nareszcie.
Wbiega i okiem chciwie ściany starodawne
Ogląda czule, jako swe znajome dawne.
Też same widzi sprzęty, też same obicia,
Z którymi się zabawiać lubił od powicia,
Lecz mniej wielkie, mniej piękne niż się dawniej zdały.
I też same portrety na ścianach wisiały:
Tu Kościuszko w czamarce krakowskiej, z oczyma
Podniesionymi w niebo, miecz oburącz trzyma;
Takim był, gdy przysięgał na stopniach ołtarzów,
Że tym mieczem wypędzi z Polski trzech mocarzów,
Albo sam na nim padnie. Dalej w polskiej szacie
Siedzi Rejtan, żałośny po wolności stracie;
W ręku trzyma nóż ostrzem zwrócony do łona,
A przed nim leży Fedon i żywot Katona.
Dalej Jasiński, młodzian piękny i posępny;
Obok Korsak, towarzysz jego nieodstępny:
Stoją na szańcach Pragi, na stosach Moskali,
Siekąc wrogów, a Praga już się wkoło pali.
Nawet stary stojący zegar kurantowy 
W drewnianej szafie poznał, u wniścia alkowy;
I z dziecinną radością pociągnął za sznurek,
By stary Dąbrowskiego usłyszeć mazurek. 
Biegał po całym domu i szukał komnaty,
Gdzie mieszkał dzieckiem będąc, przed dziesięciu laty.
Wchodzi, cofnął się, toczył zdumione źrenice
Po ścianach: w tej komnacie mieszkanie kobiéce!
Któż by tu mieszkał? Stary stryj nie był żonaty;
A ciotka w Petersburgu mieszkała przed laty.
To nie był ochmistrzyni pokój? Fortepiano?
Na nim nuty i książki; wszystko porzucano
Niedbale i bezładnie: nieporządek miły!
Niestare były rączki, co je tak rzuciły.
Tuż i sukienka biała, świeżo z kołka zdjęta
Do ubrania, na krzesła poręczu rozpięta;
A na oknach donice z pachnącymi ziołki,
Geranium, lewkonija, astry i fijołki.
Podróżny stanął w jednym z okien — nowe dziwo:
W sadzie, na brzegu niegdyś zarosłym pokrzywą,
Był maleńki ogródek ścieżkami porznięty,
Pełen bukietów trawy angielskiej i mięty.
Drewniany, drobny, w cyfrę powiązany płotek 
Połyskał się wstążkami jaskrawych stokrotek;
Grządki, widać, że były świeżo polewane,
Tuż stało wody pełne naczynie blaszane,
Ale nigdzie nie widać było ogrodniczki;
Tylko co wyszła: jeszcze kołyszą się drzwiczki
Świeżo trącone, blisko drzwi ślad widać nóżki
Na piasku, bez trzewika była i pończoszki;
Na piasku drobnym, suchym, białym na kształt śniegu,
Ślad wyraźny, lecz lekki, odgadniesz, że w biegu
Chybkim był zostawiony nóżkami drobnemi
Od kogoś, co zaledwie dotykał się ziemi.
Podróżny długo w oknie stał patrząc, dumając,
Wonnymi powiewami kwiatów oddychając.
Oblicze aż na krzaki fijołkowe skłonił,
Oczyma ciekawymi po drożynach gonił
I znowu je na drobnych śladach zatrzymywał,
Myślał o nich i, czyje były, odgadywał.
Przypadkiem oczy podniósł, i tuż na parkanie
Stała młoda dziewczyna… Białe jej ubranie
Wysmukłą postać tylko aż do piersi kryje,
Odsłaniając ramiona i łabędzią szyję.
W takim Litwinka tylko chodzić zwykła z rana,
W takim nigdy nie bywa od mężczyzn widziana:
Więc choć świadka nie miała, założyła ręce
Na piersiach, przydawając zasłony sukience.
Włos w pukle nierozwity, lecz w węzełki małe
Pokręcony, schowany w drobne strączki białe,
Dziwnie ozdabiał głowę: bo od słońca blasku
Świecił się jak korona na świętych obrazku.
Twarzy nie było widać; zwrócona na pole
Szukała kogoś okiem, daleko, na dole;
Ujrzała, zaśmiała się i klasnęła w dłonie,
Jak biały ptak zleciała z parkanu na błonie,
I wionęła ogrodem, przez płotki, przez kwiaty,
I po desce opartej o ścianę komnaty…
Nim spostrzegł się, wleciała przez okno, świecąca,
Nagła, cicha i lekka, jak światłość miesiąca.
Nucąc chwyciła suknie, biegła do zwierciadła:
Wtem ujrzała młodzieńca i z rąk jej wypadła
Suknia, a twarz od strachu i dziwu pobladła.
Twarz podróżnego barwą spłonęła rumianą,
Jak obłok, gdy z jutrzenką napotka się raną.
Skromny młodzieniec oczy zmrużył i przysłonił,
Chciał coś mówić, przepraszać; tylko się ukłonił
I cofnął się. Dziewica krzyknęła boleśnie,
Niewyraźnie, jak dziecko przestraszone we śnie;
Podróżny zląkł się, spojrzał; lecz już jej nie było. 
Wyszedł zmieszany i czuł, że mu serce biło
Głośno, i sam nie wiedział, czy go miało śmieszyć
To dziwaczne spotkanie, czy wstydzić, czy cieszyć. 
Tymczasem na folwarku nie uszło baczności,
Że przed ganek zajechał któryś z nowych gości.
Już konie w stajnią wzięto, już im hojnie dano,
Jako w porządnym domu, i obrok, i siano:
Bo Sędzia nigdy nie chciał, według nowej mody,
Odsyłać koni gości Żydom do gospody.
Słudzy nie wyszli witać; ale nie myśl wcale,
Aby w domu Sędziego służono niedbale:
Słudzy czekają, nim się pan Wojski ubierze,
Który teraz za domem urządzał wieczerzę.
On pana zastępuje i on, w niebytności
Pana, zwykł sam przyjmować i zabawiać gości
(Daleki krewny pański i przyjaciel domu). 
Widząc gościa, na folwark dążył po kryjomu,
Bo nie mógł wyjść spotykać w tkackim pudermanie;
Wdział więc jak mógł najprędzej niedzielne ubranie
Nagotowane z rana, bo od rana wiedział,
Że u wieczerzy będzie z mnóstwem gości siedział. 
Pan Wojski poznał z dala, ręce rozkrzyżował
I z krzykiem podróżnego ściskał i całował.
Zaczęła się ta prędka, zmieszana rozmowa,
W której lat kilku dzieje chciano zamknąć w słowa
Krótkie i poplątane, w ciąg powieści, pytań,
Wykrzykników i westchnień, i nowych powitań.
Gdy się pan Wojski dosyć napytał, nabadał,
Na samym końcu dzieje tego dnia powiadał. 
«Dobrze mój Tadeuszu, (bo tak nazywano
Młodzieńca, który nosił Kościuszkowskie miano
Na pamiątkę, że w czasie wojny się urodził)
Dobrze mój Tadeuszu, żeś się dziś nagodził
Do domu, właśnie kiedy mamy panien wiele.
Stryjaszek myśli wkrótce sprawić ci wesele;
Jest z czego wybrać; u nas towarzystwo liczne
Od dni kilku zbiera się na sądy graniczne,
Dla skończenia dawnego z panem Hrabią sporu.
I pan Hrabia ma jutro sam zjechać do dworu;
Podkomorzy już zjechał z żoną i z córkami.
Młodzież poszła do lasu bawić się strzelbami,
A starzy i kobiety żniwo oglądają
Pod lasem i tam pewnie na młodzież czekają.
Pójdziemy, jeśli zechcesz, i wkrótce spotkamy
Stryjaszka, Podkomorstwo i szanowne damy».
Pan Wojski z Tadeuszem idą pod las drogą,
I jeszcze się do woli nagadać nie mogą. 
Słońce ostatnich kresów nieba dochodziło,
Mniej silnie, ale szerzej niż we dnie świeciło,
Całe zaczerwienione, jak zdrowe oblicze
Gospodarza, gdy prace skończywszy rolnicze
Na spoczynek powraca. Już krąg promienisty
Spuszcza się na wierzch boru i już pomrok mglisty,
Napełniając wierzchołki i gałęzie drzewa,
Cały las wiąże w jedno i jakoby zlewa;
I bór czernił się na kształt ogromnego gmachu,
Słońce nad nim czerwone jak pożar na dachu.
Wtem zapadło do głębi; jeszcze przez konary
Błysnęło, jako świeca przez okiennic szpary,
I zgasło. I wnet sierpy gromadnie dzwoniące
We zbożach, i grabliska suwane po łące,
Ucichły i stanęły: tak pan Sędzia każe,
U niego ze dniem kończą pracę gospodarze.
«Pan świata wie, jak długo pracować potrzeba;
Słońce, Jego robotnik, kiedy znijdzie z nieba,
Czas i ziemianinowi ustępować z pola». 
Tak zwykł mawiać pan Sędzia, a Sędziego wola
Była Ekonomowi poczciwemu świętą;
Bo nawet wozy, w które już składać zaczęto
Kopę żyta, niepełne jadą do stodoły:
Cieszą się z niezwyczajnej ich lekkości woły. 
Właśnie z lasu wracało towarzystwo całe,
Wesołe, lecz w porządku. Naprzód dzieci małe
Z dozorcą, potem Sędzia szedł z Podkomorzyną,
Obok pan Podkomorzy otoczon rodziną;
Panny tuż za starszymi, a młodzież na boku;
Panny szły przed młodzieżą o jakie pół kroku
(Tak każe przyzwoitość). Nikt tam nie rozprawiał
O porządku, nikt mężczyzn i dam nie ustawiał:
A każdy mimowolnie porządku pilnował;
Bo Sędzia w domu dawne obyczaje chował,
I nigdy nie dozwalał, by chybiano względu
Dla wieku, urodzenia, rozumu, urzędu.
Tym ładem, mawiał, domy i narody słyną,
Z jego upadkiem domy i narody giną.
Więc do porządku wykli domowi i słudzy;
I przyjezdny gość, krewny albo człowiek cudzy,
Gdy Sędziego nawiedził, skoro pobył mało,
Przyjmował zwyczaj, którym wszystko oddychało. 
Krótkie były Sędziego z synowcem witania:
Dał mu poważnie rękę do pocałowania,
I w skroń ucałowawszy uprzejmie pozdrowił;
A choć przez wzgląd na gości niewiele z nim mówił,
Widać było z łez, które wylotem kontusza 
Otarł prędko, jak kochał pana Tadeusza. 
W ślad gospodarza wszystko ze żniwa i z boru,
I z łąk, i z pastwisk razem wracało do dworu.
Tu owiec trzoda becząc w ulice się tłoczy
I wznosi chmurę pyłu; dalej z wolna kroczy
Stado cielic tyrolskich z mosiężnymi dzwonki;
Tam konie rżące lecą ze skoszonej łąki:
Wszystko bieży ku studni, której ramię z drzewa
Raz wraz skrzypi i napój w koryta rozlewa.
Sędzia, choć utrudzony, chociaż w gronie gości,
Nie chybił gospodarskiej, ważnej powinności:
Udał się sam ku studni. Najlepiej z wieczora
Gospodarz widzi, w jakim stanie jest obora.
Dozoru tego nigdy sługom nie poruczy;
Bo Sędzia wie, że oko pańskie konia tuczy. 
Wojski z Woźnym Protazym ze świecami w sieni
Stali i rozprawiali, nieco poróżnieni:
Bo w niebytność Wojskiego Woźny po kryjomu
Kazał stoły z wieczerzą powynosić z domu,
I ustawić co prędzej w pośrodku zamczyska,
Którego widne były pod lasem zwaliska.
Po cóż te przenosiny? Pan Wojski się krzywił
I przepraszał Sędziego; Sędzia się zadziwił,
Lecz stało się: już późno i trudno zaradzić,
Wolał gości przeprosić i w pustki prowadzić.
Po drodze Woźny ciągle Sędziemu tłumaczył,
Dlaczego urządzenie pańskie przeinaczył:
We dworze żadna izba nie ma obszerności
Dostatecznej dla tylu, tak szanownych gości,
W zamku sień wielka, jeszcze dobrze zachowana,
Sklepienie całe — wprawdzie pękła jedna ściana,
Okna bez szyb, lecz latem nic to nie zawadzi;
Bliskość piwnic wygodna służącej czeladzi.
Tak mówiąc na Sędziego mrugał; widać z miny,
Że miał i taił inne, ważniejsze przyczyny.
O dwa tysiące kroków zamek stał za domem,
Okazały budową, poważny ogromem,
Dziedzictwo starożytnej rodziny Horeszków;
Dziedzic zginął był w czasie krajowych zamieszków.
Dobra całe zniszczone sekwestrami rządu,
Bezładnością opieki, wyrokami sądu,
W cząstce spadły dalekim krewnym po kądzieli,
A resztę rozdzielono między wierzycieli.
Zamku żaden wziąć nie chciał, bo w szlacheckim stanie
Trudno było wyłożyć koszt na utrzymanie;
Lecz Hrabia, sąsiad bliski, gdy wyszedł z opieki,
Panicz bogaty, krewny Horeszków daleki,
Przyjechawszy z wojażu upodobał mury,
Tłumacząc, że gotyckiej są architektury;
Choć Sędzia z dokumentów przekonywał o tem,
Że architekt był majstrem z Wilna, nie zaś Gotem.
Dość, że Hrabia chciał zamku. Właśnie i Sędziemu
Przyszła nagle taż chętka, nie wiadomo czemu.
Zaczęli proces w ziemstwie, potem w głównym sądzie,
W senacie, znowu w ziemstwie i guberskim rządzie;
Wreszcie, po wielu kosztach i ukazach licznych,
Sprawa wróciła znowu do sądów granicznych. 
Słusznie Woźny powiadał, że w zamkowej sieni
Zmieści się i palestra, i goście proszeni.
Sień wielka jak refektarz, z wypukłym sklepieniem
Na filarach, podłoga wysłana kamieniem,
Ściany bez żadnych ozdób, ale mur chędogi;
Sterczały wkoło sarnie i jelenie rogi
Z napisami, gdzie, kiedy te łupy zdobyte;
Tuż myśliwców herbowne klejnoty wyryte,
I stoi wypisany każdy po imieniu;
Herb Horeszków, Półkozic, jaśniał na sklepieniu.
Goście weszli w porządku i stanęli kołem.
Podkomorzy najwyższe brał miejsce za stołem;
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się damom, starcom i młodzieży.
Przy nim stał kwestarz, Sędzia tuż przy bernardynie.
Bernardyn zmówił krótki pacierz po łacinie;
Mężczyznom dano wódkę; wtenczas wszyscy siedli,
I chołodziec litewski milcząc żwawo jedli. 
Pan Tadeusz, choć młodzik, ale prawem gościa
Wysoko siadł przy damach obok jegomościa;
Między nim i stryjaszkiem jedno pozostało
Puste miejsce, jak gdyby na kogoś czekało.
Stryj nieraz na to miejsce i na drzwi poglądał,
Jakby czyjegoś przyjścia był pewny i żądał.
I Tadeusz wzrok stryja ku drzwiom odprowadzał,
I z nim na miejscu pustym oczy swe osadzał.
Dziwna rzecz! miejsca wkoło są siedzeniem dziewic,
Na które mógłby spojrzeć bez wstydu królewic,
Wszystkie zacnie zrodzone, każda młoda, ładna:
Tadeusz tam pogląda, gdzie nie siedzi żadna.
To miejsce jest zagadką; młodź lubi zagadki;
Roztargniony, do swojej nadobnej sąsiadki
Ledwo słów kilka wyrzekł, do Podkomorzanki;
Nie zmienia jej talerzów, nie nalewa szklanki,
I panien nie zabawia przez rozmowy grzeczne,
Z których by wychowanie poznano stołeczne;
To jedno puste miejsce nęci go i mami,
Już nie puste, bo on je napełnił myślami.
Po tym miejscu biegało domysłów tysiące,
Jako po deszczu żabki na samotnej łące;
Śród nich jedna króluje postać, jak w pogodę
Lilia jezior skroń białą wznosząca nad wodę.
Dano trzecią potrawę. Wtem pan Podkomorzy,
Wlawszy kropelkę wina w szklankę panny Róży,
A młodszej przysunąwszy z talerzem ogórki,
Rzekł: «Muszę ja wam służyć, moje panny córki,
Choć stary i niezgrabny». Zatem się rzuciło
Kilku młodych od stołu i pannom służyło. 
Sędzia, z boku rzuciwszy wzrok na Tadeusza
I poprawiwszy nieco wylotów kontusza,
Nalał węgrzyna i rzekł: «Dziś, nowym zwyczajem,
My na naukę młodzież do stolicy dajem;
I nie przeczym, że nasi synowie i wnuki
Mają od starych więcej książkowej nauki;
Ale co dzień postrzegam, jak młodź cierpi na tem,
Że nie ma szkół uczących żyć z ludźmi i światem.
Dawniej na dwory pańskie jachał szlachcic młody;
Ja sam lat dziesięć byłem dworskim Wojewody,
Ojca Podkomorzego, mościwego pana
(Mówiąc, Podkomorzemu ścisnął za kolana);
On mnie radą do usług publicznych sposobił,
Z opieki nie wypuścił, aż człowiekiem zrobił.
W mym domu wiecznie będzie jego pamięć droga,
Co dzień za duszę jego proszę Pana Boga.
Jeślim tyle na jego nie korzystał dworze
Jak drudzy, i wróciwszy w domu ziemię orzę,
Gdy inni, więcej godni Wojewody względów,
Doszli potem najwyższych krajowych urzędów,
Przynajmniej tom skorzystał, że mi w moim domu
Nikt nigdy nie zarzuci, bym uchybił komu
W uczciwości, w grzeczności; a powiem to śmiało,
Grzeczność nie jest nauką łatwą ani małą.
Niełatwą, bo nie na tym kończy się, jak nogą
Zręcznie wierzgnąć, z uśmiechem witać lada kogo;
Bo taka grzeczność modna, zda mi się kupiecka,
Ale nie staropolska, ani też szlachecka.
Grzeczność wszystkim należy, lecz każdemu inna;
Bo nie jest bez grzeczności i miłość dziecinna,
I wzgląd męża dla żony przy ludziach, i pana
Dla sług swoich, a w każdej jest pewna odmiana.
Trzeba się długo uczyć, ażeby nie zbłądzić
I każdemu powinną uczciwość wyrządzić.
I starzy się uczyli; u panów rozmowa,
Była to historyja żyjąca krajowa,
A między szlachtą dzieje domowe powiatu.
Dawano przez to poznać szlachcicowi bratu,
Że wszyscy o nim wiedzą, lekce go nie ważą;
Więc szlachcic obyczaje swe trzymał pod strażą. 
Dziś człowieka nie pytaj: co zacz? kto go rodzi?
Z kim on żył? co porabiał? Każdy gdzie chce wchodzi,
Byle nie szpieg rządowy i byle nie w nędzy.
Jak ów Wespazyjanus nie wąchał pieniędzy 
I nie chciał wiedzieć, skąd są, z jakich rąk i krajów,
Tak nie chcą znać człowieka rodu, obyczajów!
Dość, że ważny i że się stempel na nim widzi,
Więc szanują przyjaciół jak pieniądze Żydzi». 
To mówiąc, Sędzia gości obejrzał porządkiem;
Bo choć zawsze i płynnie mówił, i z rozsądkiem,
Wiedział, że niecierpliwa młodzież teraźniejsza,
Że ją nudzi rzecz długa, choć najwymowniejsza.
Ale wszyscy słuchali w milczeniu głębokiem.
Sędzia Podkomorzego zdał się radzić okiem;
Podkomorzy pochwałą rzeczy nie przerywał,
Ale częstym skinieniem głowy potakiwał. 
Sędzia milczał, on jeszcze skinieniem przyzwalał;
Więc Sędzia jego puchar i swój kielich nalał,
I dalej mówił: «Grzeczność nie jest rzeczą małą:
Kiedy się człowiek uczy ważyć, jak przystało,
Drugich wiek, urodzenie, cnoty, obyczaje,
Wtenczas i swoją ważność zarazem poznaje:
Jak na szalach, żebyśmy nasz ciężar poznali,
Musim kogoś posadzić na przeciwnej szali.
Zaś godna jest waszmościów uwagi osobnej
Grzeczność, którą powinna młodź dla płci nadobnej;
Zwłaszcza gdy zacność domu, fortuny szczodroty
Objaśniają wrodzone wdzięki i przymioty.
Stąd droga do afektów i stąd się kojarzy
Wspaniały domów sojusz. Tak myślili starzy.
A zatem…» Tu Pan Sędzia nagłym zwrotem głowy
Skinął na Tadeusza, rzucił wzrok surowy:
Znać było, że przychodził już do wniosków mowy.
Wtem brząknął w tabakierę złotą Podkomorzy,
I rzekł: «Mój Sędzio, dawniej było jeszcze gorzéj!
Teraz, nie wiem, czy moda i nas starych zmienia,
Czy młodzież lepsza, ale widzę mniej zgorszenia.
Ach, ja pamiętam czasy, kiedy do ojczyzny,
Pierwszy raz zawitała moda francuszczyzny!
Gdy raptem paniczyki młode z cudzych krajów
Wtargnęli do nas hordą gorszą od Nogajów,
Prześladując w ojczyźnie Boga, przodków wiarę,
Prawa i obyczaje, nawet suknie stare.
Żałośnie było widzieć wyżółkłych młokosów,
Gadających przez nosy, a często bez nosów,
Opatrzonych w broszurki i w różne gazety,
Głoszących nowe wiary, prawa, toalety.
Miała nad umysłami wielką moc ta tłuszcza;
Bo Pan Bóg, kiedy karę na naród przypuszcza,
Odbiera naprzód rozum od obywateli.
I tak, mędrsi fircykom oprzeć się nie śmieli,
I zląkł ich się jak dżumy jakiej cały naród,
Bo już sam wewnątrz siebie czuł choroby zaród.
Krzyczano na modnisiów, a brano z nich wzory;
Zmieniano wiarę, mowę, prawa i ubiory.
Była to maszkarada, zapustna swawola,
Po której miał przyjść wkrótce wielki post — niewola!
Pamiętam, chociaż byłem wtenczas małe dziecię,
Kiedy do ojca mego, w Oszmiańskim powiecie,
Przyjechał pan Podczaszyc na francuskim wózku,
Pierwszy człowiek, co w Litwie chodził po francusku.
Biegali wszyscy za nim, jakby za rarogiem,
Zazdroszczono domowi, przed którego progiem
Stanęła Podczaszyca dwukolna dryndulka,
Która się po francusku zwała karyjulka:
Zamiast lokajów, w kielni siedziały dwa pieski,
A na kozłach Niemczysko chude na kształt deski;
Nogi miał długie, cienkie jak od chmielu tyki,
W pończochach, ze srebrnymi klamrami trzewiki,
Peruka z harbajtelem zawiązanym w miechu.
Starzy na on ekwipaż parskali ze śmiechu,
A chłopi żegnali się, mówiąc: że po świecie
Jeździ wenecki diabeł w niemieckiej karecie.
Sam Podczaszyc jaki był, opisywać długo;
Dosyć, że się nam zdawał małpą lub papugą
W wielkiej peruce, którą do złotego runa
On lubił porównywać, a my do kołtuna.
Jeśli kto i czuł wtenczas, że polskie ubranie
Piękniejsze jest niż obcej mody małpowanie,
Milczał; bo by krzyczała młodzież, że przeszkadza
Kulturze, że tamuje progresy, że zdradza!
Taka była przesądów owoczesnych władza!
Podczaszyc zapowiedział, że nas reformować,
Cywilizować będzie i konstytuować;
Ogłosił nam, że jacyś Francuzi wymówni
Zrobili wynalazek: iż ludzie są równi…
Choć o tym dawno w Pańskim pisano Zakonie,
I każdy ksiądz toż samo gada na ambonie.
Nauka dawną była, szło o jej pełnienie!
Lecz wtenczas panowało takie oślepienie,
Że nie wierzono rzeczom najdawniejszym w świecie,
Jeśli ich nie czytano w francuskiej gazecie. 
Podczaszyc, mimo równość, wziął tytuł markiża;
Wiadomo, że tytuły przychodzą z Paryża,
A natenczas tam w modzie był tytuł markiża.
Jakoż, kiedy się moda odmieniła z laty,
Tenże sam markiż przybrał tytuł demokraty;
Wreszcie z odmienną modą, pod Napoleonem,
Demokrata przyjechał z Paryża baronem;
Gdyby żył dłużej, może nową alternatą,
Z barona przechrzciłby się kiedyś demokratą.
Bo Paryż częstą mody odmianą się chlubi;
A co Francuz wymyśli, to Polak polubi. 
Chwała Bogu, że teraz, jeśli nasza młodzież
Wyjeżdża za granicę, to już nie po odzież,
Nie szukać prawodawstwa w drukarskich kramarniach
Lub wymowy uczyć się w paryskich kawiarniach.
Bo teraz Napoleon, człek mądry a prędki,
Nie daje czasu szukać mody i gawędki.
Teraz grzmi oręż, a nam starym serca rosną,
Że znowu o Polakach tak na świecie głośno;
Jest sława, a więc będzie i Rzeczpospolita!
Zawżdy z wawrzynów drzewo wolności wykwita.
Tylko smutno, że nam, ach, tak się lata wleką
W nieczynności! a oni tak zawsze daleko!
Tak długo czekać! nawet tak rzadka nowina —
Ojcze Robaku (ciszej rzekł do bernardyna),
Słyszałem, żeś zza Niemna odebrał wiadomość;
Może też co o naszym wojsku wie Jegomość?»
— «Nic a nic» odpowiedział Robak obojętnie,
(Widać było, że słuchał rozmowy niechętnie)
«Mnie polityka nudzi; jeżeli z Warszawy
Mam list, to rzecz zakonna, to są nasze sprawy
Bernardyńskie: cóż o tym gadać u wieczerzy;
Są tu świeccy, do których nic to nie należy».
Tak mówiąc, spojrzał zyzem, gdzie śród biesiadników
Siedział gość, Moskal; był to pan kapitan Ryków,
Stary żołnierz, stał w bliskiej wiosce na kwaterze,
Pan Sędzia go przez grzeczność prosił na wieczerzę.
Ryków jadł smaczno, mało wdawał się w rozmowę,
Lecz na wzmiankę Warszawy, rzekł podniósłszy głowę:
«Pan Podkomorzy! Oj wy! Pan zawsze ciekawy
O Bonaparta, zawsze wam tam do Warszawy!
He! Ojczyzna! Ja nie szpieg, a po polsku umiem, —
Ojczyzna! ja to czuję wszystko, ja rozumiem!
Wy Polaki, ja Ruski: teraz się nie bijem,
Jest armistycjum, to my razem jemy, pijem.
Często na awanpostach nasz z Francuzem gada,
Pije wódkę; jak krzykną ura! — kanonada.
Ruskie przysłowie: z kim się biję, tego lubię;
Gładź drużkę jak po duszy, a bij jak po szubie.
Ja mówię, będzie wojna u nas. Do Majora
Płuta, adiutant sztabu przyjechał zawczora:
Gotować się do marszu! Pójdziem, czy pod Turka,
Czy na Francuza; oj ten Bonapart figurka!
Bez Suwarowa to on może nas wytuza. 
U nas w pułku gadano, jak szli na Francuza,
Że Bonapart czarował: no, tak i Suwarów
Czarował; tak były czary przeciw czarów.
Raz w bitwie, gdzie podział się? szukać Bonaparta,—
A on zmienił się w lisa, tak Suwarów w charta;
Tak Bonaparte znowu w kota się przerzuca,
Dalej drzeć pazurami, a Suwarów w kuca.
Obaczcież, co się stało w końcu z Bonapartą…»
Tu Ryków przerwał i jadł; wtem, z potrawą czwartą
Wszedł służący i raptem boczne drzwi otwarto.
Weszła nowa osoba przystojna i młoda.
Jej zjawienie się nagłe, jej wzrost i uroda,
Jej ubiór zwrócił oczy; wszyscy ją witali,
Prócz Tadeusza widać, że ją wszyscy znali.
Kibić miała wysmukłą, kształtną, pierś powabną,
Suknię materyjalną, różową, jedwabną,
Gors wycięty, kołnierzyk z koronek, rękawki
Krótkie; w ręku kręciła wachlarz dla zabawki
(Bo nie było gorąco); wachlarz pozłocisty
Powiewając rozlewał deszcz iskier rzęsisty;
Głowa do włosów, włosy pozwijane w kręgi,
W pukle, i przeplatane różowymi wstęgi,
Pośród nich brylant, niby zakryty od oczu,
Świecił się jako gwiazda w komety warkoczu:
Słowem, ubiór galowy; szeptali niejedni,
Że zbyt wykwintny na wieś i na dzień powszedni.
Nóżek, choć suknia krótka, oko nie zobaczy,
Bo biegła bardzo szybko, suwała się raczéj
Jako osóbki, które na trzykrólskie święta
Przesuwają w jasełkach ukryte chłopięta.
Biegła i wszystkich lekkim witając ukłonem,
Chciała usieść na miejscu sobie zostawionem:
Trudno było; bo krzeseł dla gości nie stało,
Na czterech ławach cztery ich rzędy siedziało:
Trzeba było rzęd ruszyć lub ławę przeskoczyć;
Zręcznie między dwie ławy umiała się wtłoczyć,
A potem, między rzędem siedzących i stołem,
Jak bilardowa kula toczyła się kołem.
W biegu dotknęła blisko naszego młodziana;
Uczepiwszy falbaną o czyjeś kolana,
Pośliznęła się nieco i w tym roztargnieniu
Na pana Tadeusza wsparła się ramieniu.
Przeprosiwszy go grzecznie, na miejscu swym siadła
Pomiędzy nim i stryjem, ale nic nie jadła;
Tylko się wachlowała, to wachlarza trzonek
Kręciła, to kołnierzyk z brabanckich koronek 
Poprawiała, to lekkim dotknięciem się ręki
Muskała włosów pukle i wstąg jasnych pęki.
Ta przerwa rozmów trwała już minut ze cztery.
Tymczasem, w końcu stoła, naprzód ciche szmery,
A potem się zaczęły wpół głośne rozmowy;
Mężczyźni rozsądzali swe dzisiejsze łowy.
Asesora z Rejentem wzmogła się uparta
Coraz głośniejsza kłótnia o kusego charta,
Którego posiadaniem pan Rejent się szczycił
I utrzymywał, że on zająca pochwycił;
Asesor zaś dowodził na złość Rejentowi,
Że ta chwała należy chartu Sokołowi.
Pytano zdania innych; więc wszyscy dokoła
Brali stronę Kusego albo też Sokoła,
Ci jak znawcy, ci znowu jak naoczne świadki. 
Sędzia na drugim końcu do nowej sąsiadki
Rzekł półgłosem: «Przepraszam, musieliśmy siadać,
Nie podobna wieczerzy na później odkładać:
Goście głodni, chodzili daleko na pole;
Myśliłem, że dziś z nami nie będziesz przy stole». 
To rzekłszy, z Podkomorzym przy pełnym kielichu
O politycznych sprawach rozmawiał po cichu.
Gdy tak były zajęte stołu strony obie,
Tadeusz przyglądał się nieznanej osobie.
Przypomniał, że za pierwszym na miejsce wejrzeniem
Odgadnął zaraz, czyim miało być siedzeniem.
Rumienił się, serce mu biło nadzwyczajnie:
Więc rozwiązane widział swych domysłów tajnie!
Więc było przeznaczono, by przy jego boku
Usiadła owa piękność widziana w pomroku!
Wprawdzie zdała się teraz wzrostem dorodniejsza,
Bo ubrana, a ubiór powiększa i zmniejsza.
I włos u tamtej widział krótki, jasnozłoty,
A u tej krucze długie zwijały się sploty?
Kolor musiał pochodzić od słońca promieni,
Którymi przy zachodzie wszystko się czerwieni.
Twarzy wówczas nie dostrzegł, nazbyt rychło znikła;
Ale myśl twarz nadobną odgadywać zwykła:
Myślił, że pewnie miała czarniutkie oczęta,
Białą twarz, usta kraśne jak wiśnie bliźnięta;
U tej znalazł podobne oczy, usta, lica.
W wieku może by była największa różnica:
Ogrodniczka dziewczynką zdawała się małą,
A pani ta niewiastą już w latach dojrzałą;
Lecz młodzież o piękności metrykę nie pyta,
Bo młodzieńcowi młodą jest każda kobiéta,
Chłopcowi każda piękność zda się rówiennicą,
A niewinnemu każda kochanka dziewicą. 
Tadeusz, chociaż liczył lat blisko dwadzieście,
I od dzieciństwa mieszkał w Wilnie, wielkim mieście,
Miał za dozorcę księdza, który go pilnował
I w dawnej surowości prawidłach wychował.
Tadeusz zatem przywiózł w strony swe rodzinne
Duszę czystą, myśl żywą i serce niewinne,
Ale razem niemałą chętkę do swawoli.
Z góry już robił projekt, że sobie pozwoli
Używać na wsi długo wzbronionej swobody;
Wiedział, że był przystojny, czuł się rześki, młody,
A w spadku po rodzicach wziął czerstwość i zdrowie.
Nazywał się Soplica: wszyscy Soplicowie
Są, jak wiadomo, krzepcy, otyli i silni,
Do żołnierki jedyni, w naukach mniej pilni.
Tadeusz się od przodków swoich nie odrodził:
Dobrze na koniu jeździł, pieszo dzielnie chodził,
Tępy nie był, lecz mało w naukach postąpił,
Choć stryj na wychowanie niczego nie skąpił;
On wolał z flinty strzelać albo szablą robić.
Wiedział, że go myślano do wojska sposobić,
Że ojciec w testamencie wyrzekł taką wolę;
Ustawicznie do bębna tęsknił, siedząc w szkole.
Ale stryj nagle pierwsze zamiary odmienił,
Kazał, aby przyjechał i aby się żenił
I objął gospodarstwo; przyrzekł na początek
Dać małą wieś, a potem cały swój majątek.
Te wszystkie Tadeusza cnoty i zalety
Ściągnęły wzrok sąsiadki, uważnej kobiety.
Zmierzyła jego postać kształtną i wysoką,
Jego ramiona silne, jego pierś szeroką,
I w twarz spojrzała, z której wytryskał rumieniec,
Ilekroć z jej oczyma spotkał się młodzieniec:
Bo z pierwszej lękliwości całkiem już ochłonął,
I patrzył wzrokiem śmiałym, w którym ogień płonął.
Również patrzyła ona: i cztery źrenice
Gorzały przeciw sobie jak roratne świéce. 
Pierwsza z nim po francusku zaczęła rozmowę.
Wracał z miasta, ze szkoły: więc o książki nowe,
O autorów pytała Tadeusza zdania
I ze zdań wyciągała na nowo pytania.
Cóż, gdy potem zaczęła mówić o malarstwie,
O muzyce, o tańcach, nawet o rzeźbiarstwie,
Dowiodła, że zna równie pędzel, nuty, druki;
Aż osłupiał Tadeusz na tyle nauki!
Lękał się, by nie został pośmiewiska celem,
I jąkał się jak żaczek przed nauczycielem.
Szczęściem, że nauczyciel ładny i niesrogi;
Odgadnęła sąsiadka powód jego trwogi,
Wszczęła rzecz o mniej trudnych i mądrych przedmiotach,
O wiejskiego pożycia nudach i kłopotach,
I jak bawić się trzeba, i jak czas podzielić,
By życie uprzyjemnić i wieś rozweselić.
Tadeusz odpowiadał śmielej, szła rzecz daléj,
W pół godziny już byli z sobą poufali;
Zaczęli nawet małe żarciki i sprzeczki.
W końcu, stawiła przed nim trzy z chleba gałeczki.
Trzy osoby na wybór; wziął najbliższą sobie;
Podkomorzanki na to zmarszczyły się obie,
Sąsiadka zaśmiała się, lecz nie powiedziała
Kogo owa szczęśliwsza gałka oznaczała. 
Inaczej bawiono się w drugim końcu stoła;
Bo tam, wzmogłszy się nagle, stronnicy Sokoła
Na partyję Kusego bez litości wsiedli.
Spór był wielki, już potraw ostatnich nie jedli;
Stojąc i pijąc obie kłóciły się strony,
A najstraszniej pan Rejent był zacietrzewiony:
Jak raz zaczął, bez przerwy rzecz swoją tokował,
I gestami ją bardzo dobitnie malował.
(Był dawniej adwokatem pan Rejent Bolesta,
Zwano go kaznodzieją, że zbyt lubił gesta).
Teraz ręce przy boku miał, w tył wygiął łokcie,
Spod ramion wytknął palce i długie paznokcie,
Przedstawiając dwa smycze chartów tym obrazem:
Właśnie rzecz kończył. «Wyczha! puściliśmy razem
Ja i Asesor, razem, jakoby dwa kurki
Jednym palcem spuszczone u jednej dwururki;
Wyczha! poszli, a zając jak struna, smyk w pole,
Psy tuż (to mówiąc, ręce ciągnął wzdłuż po stole
I palcami ruch chartów przedziwnie udawał)
Psy tuż, i hec od lasu odsadzili kawał;
Sokół smyk naprzód; rączy pies, lecz zagorzalec,
Wysadził się przed Kusym, o tyle, o palec:
Wiedziałem, że spudłuje. Szarak, gracz nie lada,
Czchał niby prosto w pole, za nim psów gromada;
Gracz szarak! Skoro poczuł wszystkie charty w kupie
Pstręk na prawo, koziołka, z nim w prawo psy głupie,
A on znowu fajt w lewo, jak wytnie dwa susy,
Psy za nim fajt na lewo: on w las, a mój Kusy
Cap!» Tak krzycząc, pan Rejent na stół pochylony,
Z palcami swymi zabiegł aż do drugiej strony,
I «cap!» Tadeuszowi wrzasnął tuż nad uchem:
Tadeusz i sąsiadka, tym głosu wybuchem
Znienacka przestraszeni właśnie w pół rozmowy,
Odstrychnęli od siebie mimowolnie głowy,
Jako wierzchołki drzewa powiązane społem
Gdy je wicher rozerwie; i ręce pod stołem
Blisko siebie leżące wstecz nagle uciekły,
I dwie twarze w jeden się rumieniec oblekły.
Tadeusz, by nie zdradzić swego roztargnienia:
«Prawda — rzekł — mój Rejencie, prawda bez wątpienia,
Kusy piękny chart z kształtu, jeśli równie chwytny…»
«Chwytny? — krzyknął pan Rejent — mój pies faworytny
Żeby nie miał być chwytny?…» Więc Tadeusz znowu
Cieszył się, że tak piękny pies nie ma narowu,
Żałował, że go tylko widział idąc z lasu,
I że przymiotów jego poznać nie miał czasu.
Na to zadrżał Asesor, puścił z rąk kieliszek,
Utopił w Tadeusza wzrok jak bazyliszek.
Asesor mniej krzykliwy i mniej był ruchawy
Od Rejenta, szczuplejszy i mały z postawy,
Lecz straszny na reducie, balu i sejmiku,
Bo powiadano o nim: ma żądło w języku;
Tak dowcipne żarciki umiał komponować,
Iżby je w kalendarzu można wydrukować,
Wszystkie złośliwe, ostre. Dawniej człek dostatni,
Schedę ojca swojego i majątek bratni
Wszystko strwonił na wielkim figurując świecie;
Teraz wszedł w służbę rządu, by znaczyć w powiecie.
Lubił bardzo myślistwo, już to dla zabawy,
Już to że odgłos trąbki i widok obławy
Przypominał mu jego lata młodociane,
Kiedy miał strzelców licznych i psy zawołane:
Teraz mu z całej psiarni dwa charty zostały,
I jeszcze z tych jednemu chciano przeczyć chwały!
Więc zbliżył się i z wolna gładząc faworyty
Rzekł z uśmiechem, a był to uśmiech jadowity:
«Chart bez ogona jest jak szlachcic bez urzędu,
Ogon też znacznie chartom pomaga do pędu:
A pan kusość uważasz za dowód dobroci?
Zresztą zdać się możemy na sąd pańskiej cioci.
Choć pani Telimena mieszkała w stolicy
I bawi się niedawno w naszej okolicy,
Lepiej zna się na łowach niż myśliwi młodzi:
Tak to nauka sama z latami przychodzi».
Tadeusz, na którego niespodzianie spadał
Grom taki, wstał zmieszany, chwilę nic nie gadał,
Lecz patrzał na rywala coraz straszniej, srożej… 
Wtem, wielkim szczęściem, dwakroć kichnął Podkomorzy
«Wiwat!» krzyknęli wszyscy; on się wszystkim skłonił
I z wolna w tabakierę palcami zadzwonił.
Tabakiera ze złota, z brylantów oprawa,
A w środku jej był portret króla Stanisława.
Ojcu Podkomorzego sam król ją darował,
Po ojcu Podkomorzy godnie ją piastował;
Gdy w nią dzwonił, znak dawał, że miał głos zabierać.
Umilkli wszyscy i ust nie śmieli otwierać.
On rzekł: «Wielmożni szlachta bracia dobrodzieje,
Forum myśliwskim tylko są łąki i knieje;
Więc ja w domu podobnych spraw nie decyduję,
I posiedzenie nasze na jutro solwuję,
I dalszych replik stronom dzisiaj nie dozwolę.
Woźny! odwołaj sprawę, na jutro na pole.
Jutro i Hrabia z całym myślistwem tu zjedzie,
I waszeć z nami ruszysz, Sędzio mój sąsiedzie,
I pani Telimena, i panny, i panie,
Słowem, zrobim na urząd wielkie polowanie;
I Wojski towarzystwa nam też nie odmówi».
To mówiąc, tabakierę podawał starcowi.
Wojski na ostrym końcu śród myśliwych siedział,
Słuchał zmrużywszy oczy, słowa nie powiedział,
Choć młodzież nieraz jego zasięgała zdania,
Bo nikt lepiej nad niego nie znał polowania.
On milczał, szczyptę wziętą z tabakiery ważył
W palcach i długo dumał, nim ją w końcu zażył;
Kichnął, aż cała izba rozległa się echem,
I potrząsając głową, rzekł z gorzkim uśmiechem:
«O, jak mnie to starego i smuci, i dziwi!
Cóż by to o tym starzy mówili myśliwi,
Widząc że w tylu szlachty, w tylu panów gronie,
Mają sądzić się spory o charcim ogonie?
Cóż by rzekł na to stary Rejtan, gdyby ożył?
Wróciłby do Lachowicz i w grób się położył!
Co by rzekł wojewoda Niesiołowski stary,
Który ma dotąd pierwsze na świecie ogary,
I dwiestu strzelców trzyma obyczajem pańskim,
I ma sto wozów sieci w zamku Worończańskim,
A od tylu lat siedzi jak mnich na swym dworze,
Nikt go na polowanie uprosić nie może,
Białopiotrowiczowi samemu odmówił!
Bo cóż by on na waszych polowaniach łowił?
Piękna byłaby sława, ażeby pan taki
Wedle dzisiejszej mody jeździł na szaraki!
Za moich, panie, czasów, w języku strzeleckim,
Dzik, niedźwiedź, łoś, wilk, zwany był zwierzem szlacheckim
A zwierzę niemające kłów, rogów, pazurów,
Zostawiano dla płatnych sług i dworskich ciurów;
Żaden pan nigdy przyjąć nie chciałby do ręki
Strzelby, którą zhańbiono sypiąc w nią śrut cienki!
Trzymano wprawdzie chartów: bo z łowów wracając,
Trafia się, że spod konia mknie się biedak zając:
Puszczano wtenczas za nim dla zabawki smycze
I na konikach małe goniły panicze
Przed oczyma rodziców, którzy te pogonie
Ledwie raczyli widzieć, cóż kłócić się o nie!
Więc niech jaśnie wielmożny Podkomorzy raczy
Odwołać swe rozkazy i niech mi wybaczy,
Że nie mogę na takie jechać polowanie,
I nigdy na nim noga moja nie postanie!
Nazywam się Hreczecha, a od króla Lecha,
Żaden za zającami nie jeździł Hreczecha». 
Tu śmiech młodzieży mowę Wojskiego zagłuszył.
Wstano od stołu, pierwszy Podkomorzy ruszył,
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się damom, starcom i młodzieży;
Za nim szedł kwestarz, Sędzia tuż przy bernardynie.
Sędzia u progu rękę dał Podkomorzynie,
Tadeusz Telimenie, Asesor Krajczance,
A pan Rejent na końcu Wojskiej Hreczeszance.
Tadeusz z kilku gośćmi poszedł do stodoły,
A czuł się pomieszany, zły i niewesoły.
Rozbierał myślą wszystkie dzisiejsze wypadki:
Spotkanie się, wieczerzę przy boku sąsiadki;
A szczególniej mu słowo «ciocia» koło ucha
Brzęczało ciągle jako naprzykrzona mucha.
Pragnąłby u Woźnego lepiej się wypytać
O pani Telimenie, lecz go nie mógł schwytać;
Wojskiego też nie widział, bo zaraz z wieczerzy
Wszyscy poszli za gośćmi, jak sługom należy,
Urządzając we dworze izby do spoczynku.
Starsi i damy spały we dworskim budynku;
Młodzież Tadeuszowi prowadzić kazano,
W zastępstwie gospodarza, w stodołę na siano. 
W pół godziny tak było głucho w całym dworze
jako po zadzwonieniu na pacierz w klasztorze;
Ciszę przerywał tylko głos nocnego stróża.
Usnęli wszyscy. Sędzia sam oczu nie zmruża;
Jako wódz gospodarstwa obmyśla wyprawę
W pole i w domu przyszłą urządza zabawę.
Dał rozkaz ekonomom, wójtom i gumiennym,
Pisarzom, ochmistrzyni, strzelcom i stajennym
I musiał wszystkie dzienne rachunki przezierać.
Nareszcie rzekł Woźnemu, że się chce rozbierać. 
Woźny pas mu odwiązał, pas słucki, pas lity,
Przy którym świecą gęste kutasy jak kity,
Z jednej strony złotogłów w purpurowe kwiaty,
Na wywrót jedwab czarny posrebrzany w kraty;
Pas taki można równie kłaść na strony obie,
Złotą na dzień galowy, a czarną w żałobie.
Sam Woźny umiał pas ten odwiązywać, składać;
Właśnie tym się zatrudniał i kończył tak gadać:
«Cóż złego, że przeniosłem stoły do zamczyska?
Nikt na tym nic nie stracił, a pan może zyska.
Bo przecież o ten zamek dziś toczy się sprawa.
My od dzisiaj do zamku nabyliśmy prawa
I mimo całą strony przeciwnej zajadłość
Dowiodę, że zamczysko wzięliśmy w posiadłość.
Wszakże kto gości prosi w zamek na wieczerzę,
Dowodzi, że posiadłość tam ma albo bierze;
Nawet strony przeciwne weźmiemy na świadki:
Pamiętam za mych czasów podobne wypadki».
Już Sędzia spał. Więc Woźny cicho wszedł do sieni,
Siadł przy świecy i dobył książeczkę z kieszeni,
Która mu jak Ołtarzyk Złoty zawsze służy,
Której nigdy nie rzuca w domu i w podróży.
Była to trybunalska wokanda: tam rzędem
Stały spisane sprawy, które przed urzędem
Woźny sam głosem swoim przed laty wywołał,
Albo o których później dowiedzieć się zdołał.
Prostym ludziom wokanda zda się imion spisem;
Woźnemu jest obrazów wspaniałych zarysem.
Czytał więc i rozmyślał: Ogiński z Wizgirdem,
Dominikanie z Rymszą, Rymsza z Wysogirdem,
Radziwił z Wereszczaką, Giedroić z Rdułtowskim,
Obuchowicz z kahałem, Juraha z Piotrowskim,
Maleski z Mickiewiczem, a na koniec Hrabia
Z Soplicą; i czytając, z tych imion wywabia
Pamięć spraw wielkich, wszystkie procesu wypadki,
I stają mu przed oczy sąd, strony i świadki;
I ogląda sam siebie, jak w żupanie białym,
W granatowym kontuszu stał przed trybunałem,
Jedna ręka na szabli, a druga do stoła,
Przywoławszy dwie strony, «Uciszcie się!» woła.
Marząc i kończąc pacierz wieczorny, pomału
Usnął ostatni w Litwie woźny trybunału. 
Takie były zabawy, spory w one lata
Śród cichej wsi litewskiej, kiedy reszta świata
We łzach i krwi tonęła; gdy ów mąż, bóg wojny,
Otoczon chmurą pułków, tysiącem dział zbrojny,
Wprzągłszy w swój rydwan orły złote obok srebrnych,
Od puszcz Libijskich łatał do Alpów podniebnych,
Ciskając grom po gromie, w Piramidy, w Tabor,
W Marengo, w Ulm, w Austerlitz. Zwycięstwo i Zabor
Biegły przed nim i za nim. Sława czynów tylu,
Brzemienna imionami rycerzy, od Nilu
Szła hucząc ku północy, aż u Niemna brzegów
Odbiła się, jak od skał, od Moskwy szeregów,
Które broniły Litwę murami żelaza
Przed wieścią dla Rosyi straszną jak zaraza. 
Przecież nieraz nowina niby kamień z nieba
Spadała w Litwę. Nieraz dziad żebrzący chleba,
Bez ręki lub bez nogi, przyjąwszy jałmużnę,
Stanął i oczy wkoło obracał ostróżne.
Gdy nie widział we dworze rosyjskich żołnierzy
Ani jarmułek, ani czerwonych kołnierzy,
Wtenczas kim był, wyznawał: był legijonistą,
Przynosi kości stare na ziemię ojczystą,
Której już bronić nie mógł… Jak go wtenczas cała
Rodzina pańska, jak go czeladka ściskała,
Zanosząc się od płaczu! On za stołem siadał
I dziwniejsze od baśni historyje gadał. 
On opowiadał, jako jenerał Dąbrowski,
Z ziemi włoskiej stara się przyciągnąć do Polski,
Jak on rodaków zbiera na lombardzkim polu;
Jak Kniaziewicz rozkazy daje z Kapitolu
I zwycięzca, wydartych potomkom cezarów
Rzucił w oczy Francuzów sto krwawych sztandarów,
Jak Jabłonowski zabiegł, aż kędy pieprz rośnie,
Gdzie się cukier wytapia i gdzie w wiecznej wiośnie
Pachnące kwitną lasy; z legiją Dunaju
Tam wódz Murzyny gromi, a wzdycha do kraju.
Mowy starca krążyły we wsi po kryjomu;
Chłopiec, co je posłyszał, znikał nagle z domu,
Lasami i bagnami skradał się tajemnie,
Ścigany od Moskali, skakał kryć się w Niemnie
I nurkiem płynął na brzeg Księstwa Warszawskiego,
Gdzie usłyszał głos miły: «Witaj nam kolego!»
Lecz nim odszedł, wyskoczył na wzgórek z kamienia
I Moskalom przez Niemen rzekł: «Do zobaczenia!»
Tak przekradł się Gorecki, Pac i Obuchowicz,
Piotrowski, Obolewski, Rożycki, Janowicz,
Mierzejewscy, Brochocki i Bernatowicze,
Kupść, Gedymin i inni, których nie policzę:
Opuszczali rodziców i ziemię kochaną,
I dobra, które na skarb carski zabierano. 
Czasem do Litwy kwestarz z obcego klasztoru
Przyszedł, i kiedy bliżej poznał panów dworu,
Gazetę im pokazał, wyprutą z szkaplerza.
Tam stała wypisana i liczba żołnierza,
I nazwisko każdego wodza legijonu,
I każdego z nich opis zwycięstwa lub zgonu.
Po wielu latach pierwszy raz miała rodzina
Wieść o życiu, o chwale i o śmierci syna;
Brał dom żałobę, ale powiedzieć nie śmiano
Po kim była żałoba, tylko zgadywano
W okolicy; i tylko cichy smutek panów,
Lub cicha radość, była gazetą ziemianów. 
Takim kwestarzem tajnym był Robak podobno:
Często on z panem Sędzią rozmawiał osobno;
Po tych rozmowach zawsze jakowaś nowina
Rozeszła się w sąsiedztwie. Postać bernardyna
Wydawała, że mnich ten nie zawsze w kapturze
Chodził i nie w klasztornym zestarzał się murze.
Miał on nad prawym uchem, nieco wyżej skroni,
Bliznę, wyciętej skóry na szerokość dłoni,
I w brodzie ślad niedawny lancy lub postrzału;
Ran tych nie dostał pewnie przy czytaniu mszału.
Ale nie tylko groźne wejrzenie i blizny,
Lecz sam ruch i głos jego miał coś żołnierszczyzny.
Przy mszy, gdy z wzniesionymi zwracał się rękami
Od ołtarza do ludu, by mówić: «Pan z wami»,
To nieraz tak się zręcznie skręcił jednym razem,
Jakby prawo w tył robił za wodza rozkazem,
I słowa liturgii takim wyrzekł tonem
Do ludu, jak oficer stojąc przed szwadronem:
Postrzegali to chłopcy służący mu do mszy. 
Spraw także politycznych był Robak świadomszy,
Niźli żywotów świętych; a jeżdżąc po kweście,
Często zastanawiał się w powiatowym mieście.
Miał pełno interesów: to listy odbierał,
Których nigdy przy obcych ludziach nie otwierał,
To wysyłał posłańców, ale gdzie i po co
Nie powiadał; częstokroć wymykał się nocą
Do dworów pańskich, z szlachtą ustawicznie szeptał,
I okoliczne wioski dokoła wydeptał,
I w karczmach z wieśniakami rozprawiał niemało,
A zawsze o tym, co się w cudzych krajach działo.
Teraz Sędziego, który już spał od godziny,
Przychodzi budzić; pewnie ma jakieś nowiny.
Księga druga
Zamek
Polowanie z chartami na upatrzonego — Gość w zamku — Ostatni z dworzan opowiada historię ostatniego z Horeszków — Rzut oka w sad — Dziewczyna w ogórkach — Śniadanie — Pani Telimeny anegdota petersburska — Nowy wybuch sporów o Kusego i Sokoła — Interwencja Robaka — Rzecz Wojskiego — Zakład — Dalej w grzyby!

Kto z nas tych lat nie pomni, gdy, młode pacholę,
Ze strzelbą na ramieniu świszcząc szedł na pole,
Gdzie żaden wał, płot żaden nogi nie utrudza,
Gdzie, przestępując miedzę, nie poznasz, że cudza!
Bo na Litwie myśliwiec jak okręt na morzu,
Gdzie chcesz, jaką chcesz drogą, buja po przestworzu:
Czyli jak prorok patrzy w niebo, gdzie w obłoku
Wiele jest znaków widnych strzeleckiemu oku;
Czy jak czarownik gada z ziemią, która, głucha
Dla mieszczan, mnóstwem głosów szepce mu do ucha. 
Tam derkacz wrzasnął z łąki, szukać go daremnie,
Bo on szybuje w trawie jako szczupak w Niemnie;
Tam ozwał się nad głową ranny wiosny dzwonek,
Również głęboko w niebie schowany skowronek;
Ówdzie orzeł szerokim skrzydłem przez obszary
Zaszumiał, strasząc wróble, jak kometa cary;
Zaś jastrząb, pod jasnymi wiszący błękity,
Trzepie skrzydłem jak motyl na szpilce przybity,
Aż ujrzawszy wśród łąki ptaka lub zająca,
Runie nań z góry jako gwiazda spadająca. 
Kiedyż nam Pan Bóg wrócić z wędrówki dozwoli,
I znowu dom zamieszkać na ojczystej roli,
I służyć w jeździe, która wojuje szaraki,
Albo w piechocie, która nosi broń na ptaki,
Nie znać innych prócz kosy i sierpa rynsztunków,
I innych gazet, oprócz domowych rachunków!
Nad Soplicowem słońce weszło i już padło
Na strzechy i przez szpary w stodołę się wkradło;
I po ciemnozielonym, świeżym, wonnym sianie,
Z którego młodzież sobie zrobiła posłanie,
Rozpływały się złote, migające pręgi
Z otworu czarnej strzechy jak z warkocza wstęgi;
I słońce usta sennych promykiem poranka
Drażni jak dziewczę kłosem budzące kochanka. 
Już wróble skacząc, świerkać zaczęły pod strzechą;
Już trzykroć gęgnął gąsior, a za nim jak echo
Odezwały się chórem kaczki i indyki
I słychać bydła w pole idącego ryki. 
Wstała młodzież. Tadeusz jeszcze senny leży;
Bo też najpóźniej zasnął. Z wczorajszej wieczerzy
Wrócił tak niespokojny, że o kurów pianiu
Jeszcze oczu nie zmrużył, a na swym posłaniu
Tak kręcił się, że w siano jak w wodę utonął,
I spał twardo, aż zimny wiatr w oczy mu wionął,
Gdy skrzypiące stodoły drzwi otwarto z trzaskiem,
I bernardyn, ksiądz Robak, wszedł z węzlastym paskiem,
«Surge puer!» wołając i ponad barkami
Rubasznie wywijając pasek z ogórkami.
Już na dziedzińcu słychać myśliwskie okrzyki;
Wyprowadzają konie, zajeżdżają bryki,
Ledwie dziedziniec taką gromadę ogarnie,
Odezwały się trąby, otworzono psiarnie;
Zgraja chartów, wypadłszy, wesoło skowycze;
Widząc rumaki szczwaczów, dojeżdżaczów smycze,
Psy jak szalone cwałem śmigają po dworze,
Potem biegną i kładą szyje na obroże:
Wszystko to bardzo dobre polowanie wróży;
Nareszcie Podkomorzy dał rozkaz podróży.
Ruszyli szczwacze z wolna, jeden tuż za drugim;
Ale za bramą rzędem rozbiegli się długim.
W środku jechali obok Asesor z Rejentem;
A choć na siebie czasem patrzyli ze wstrętem,
Rozmawiali przyjaźnie, jak ludzie honoru
Idąc na rozstrzygnienie śmiertelnego sporu:
Nikt ze słów zawziętości ich poznać nie zdoła;
Pan Rejent wiódł Kusego, Asesor Sokoła.
Z tyłu damy w pojazdach; młodzieńcy, stronami
Cwałując tuż przy kołach, gadali z damami.
Ksiądz Robak po dziedzińcu wolnym chodził krokiem
Kończąc ranne pacierze; ale rzucał okiem
Na pana Tadeusza, marszczył się, uśmiechał,
Wreszcie kiwnął nań palcem, Tadeusz podjechał;
Robak palcem po nosie dawał mu znak groźby:
Lecz mimo Tadeusza pytania i prośby,
Ażeby mu wyraźnie, co chce, wytłumaczył,
Bernardyn odpowiedzieć ni spojrzeć nie raczył;
Kaptur tylko nasunął i pacierz swój kończył,
Więc Tadeusz odjechał i z gośćmi się złączył.
Właśnie wtenczas myśliwi smycze zatrzymali,
I wszyscy nieruchomi w miejscach swoich stali;
Jeden drugiemu ręką dawał znak milczenia,
A wszyscy obrócili oczy do kamienia,
Nad którym stał pan Sędzia. On zwierza obaczył
I rąk skinieniem swoje rozkazy tłumaczył.
Pojęli wszyscy: stoją, a środkiem po roli
Asesor i pan Rejent kłusują powoli.
Tadeusz, będąc bliższy, obydwu wyprzedził,
Stanął obok Sędziego i oczyma śledził.
Dawno już nie był w polu; na szarej przestrzeni
Trudno dojrzeć szaraka, zwłaszcza śród kamieni.
Pokazał mu pan Sędzia; siedział biedny zając,
Płaszcząc się pod kamieniem, uszy nadstawiając,
Okiem czerwonym spotkał myśliwców wejrzenie
I jakby urzeczony, czując przeznaczenie,
Ze strachu od ich oczu nie mógł zwrócić oka,
I pod opoką siedział martwy jak opoka. 
Tymczasem kurz na roli rośnie coraz bliżéj;
Pędzi na smyczy Kusy, za nim Sokół chyży,
Tuż Asesor z Rejentem razem wrzaśli z tyłu:
«Wyczha, wyczha!» i z psami znikli w kłębach pyłu. 
Kiedy tak za szarakiem goniono, tymczasem
Ukazał się pan Hrabia pod zamkowym lasem.
Wiedziano w okolicy, że ten pan nie może
Nigdy nigdzie stawić się w naznaczonej porze.
I dziś zaspał poranek; więc na sługi zrzędził,
Widząc myśliwców w polu cwałem do nich pędził.
Surdut swój angielskiego kroju, biały, długi,
Połami na wiatr puścił; z tyłu konno sługi,
W kapeluszach jak grzybki, czarnych, lśniących, małych,
W kurtkach, w butach stryflastych, w pantalonach białych:
Sługi, które pan Hrabia tym kształtem odzieje,
Nazywają się w jego pałacu dżokeje. 
Cwałująca czereda zleciała na błonia,
Gdy Hrabia ujrzał zamek i zatrzymał konia.
Pierwszy raz widział zamek z rana i nie wierzył,
Że to były też same mury; tak odświeżył
I upięknił poranek zarysy budowy:
Zadziwił się pan Hrabia na widok tak nowy.
Wieża zdała się dwakroć wyższa, bo stercząca
Nad mgłą ranną; dach z blachy złocił się od słońca,
Pod nim błyszczała w kratach reszta szyb wybitych,
Łamiąc promienie wschodu w tęczach rozmaitych;
Niższe piętra oblała tumanu powłoka,
Rozpadliny i szczerby zakryła od oka;
Krzyk dalekich myśliwców wiatrami przygnany,
Odbijał się kilkakroć o zamkowe ściany:
Przysiągłbyś, że krzyk z zamku, że pod mgły zasłoną
Mury odbudowano i znów zaludniono. 
Hrabia lubił widoki niezwykłe i nowe,
Zwał je romansowymi; mawiał, że ma głowę
Romansową: w istocie był wielkim dziwakiem.
Nieraz, pędząc za lisem albo za szarakiem,
Nagle stawał i w niebo poglądał żałośnie,
Jak kot, gdy ujrzy wróble na wysokiej sośnie;
Często bez psa, bez strzelby, błąkał się po gaju
Jak rekrut zbiegły; często siadał przy ruczaju
Nieruchomy, schyliwszy głowę nad potokiem,
Jak czapla wszystkie ryby chcąca pozrzeć okiem:
Takie były Hrabiego dziwne obyczaje.
Wszyscy mówili, że mu czegoś nie dostaje;
Szanowano go przecież, bo pan z prapradziadów,
Bogacz, dobry dla chłopów, ludzki dla sąsiadów,
Nawet dla Żydów. 
Hrabski koń, zwrócony z drogi,
Prosto kłusował polem aż pod zamku progi.
Hrabia samotny wzdychał, poglądał na mury,
Wyjął papier, ołówek i kreślił figury.
Wtem, spojrzawszy w bok — ujrzał o dwadzieścia kroków
Człowieka, który, równie miłośnik widoków,
Z głową zadartą, ręce włożywszy w kieszenie,
Zdawało się, że liczył oczyma kamienie.
Poznał go zaraz, ale musiał kilka razy
Krzyknąć, nim głos Hrabiego usłyszał Gerwazy.
Szlachcic to był, służący dawnych zamku panów,
Pozostały ostatni z Horeszki dworzanów;
Starzec wysoki, siwy, twarz miał czerstwą, zdrową,
Zmarszczkami pooraną, posępną, surową.
Dawniej pomiędzy szlachtą z wesołości słynął;
Ale od bitwy, w której dziedzic zamku zginął,
Gerwazy się odmienił i już od lat wielu
Ani był na kiermaszu, ani na weselu;
Odtąd jego dowcipnych żartów nie słyszano,
I uśmiechu na jego twarzy nie widziano.
Zawsze nosił Horeszków liberyją dawną;
Kurtę z połami żółtą, galonem oprawną,
Który dziś żółty, dawniej zapewne był złoty,
Wkoło szyte jedwabiem herbowe klejnoty,
Półkozice: i stąd też cała okolica
Półkozicem przezwała starego szlachcica.
Czasem też od przysłowia, które bez ustanku
Powtarzał, nazywano go także Mopanku;
Czasem Szczerbcem, że całą łysinę miał w szczerbach;
Lecz on zwał się Rębajło, a o jego herbach
Nie wiadomo. Klucznikiem siebie tytułował,
Iż ten urząd na zamku przed laty piastował.
I dotąd nosił wielki pęk kluczy za pasem,
Uwiązany na taśmie ze srebrnym kutasem,
Choć nie miał co otwierać, bo zamku podwoje
Stały otworem. Przecież, wynalazł drzwi dwoje;
Sam je własnym nakładem naprawił i wstawił,
I drzwi tych odmykaniem codziennie się bawił.
W jednej z izb pustych, obrał mieszkanie dla siebie;
Mogąc żyć u Hrabiego na łaskawym chlebie,
Nie chciał, bo wszędzie tęsknił i czuł się niezdrowym,
Jeżeli nie oddychał powietrzem zamkowym.
Skoro ujrzał Hrabiego, czapkę z głowy schwycił,
I krewnego swych panów ukłonem zaszczycił,
Chyląc łysinę wielką, świecącą z daleka,
I naciętą od licznych kordów jak nasieka;
Gładził ją ręką, podszedł, i jeszcze raz nisko
Skłoniwszy się, rzekł smutnie: «Mopanku, panisko,
Daruj mnie, że tak mówię, jaśnie grafie panie,
To jest mój zwyczaj, nie zaś nieuszanowanie:
»mopanku« powiadali wszyscy Horeszkowie,
Ostatni Stolnik, pan mój, miał takie przysłowie… 
Czyż to prawda, mopanku, że pan grosza skąpisz
Na proces i ten zamek Soplicom ustąpisz?
Nie wierzyłem, lecz w całym powiecie tak słychać».
Tu, poglądając w zamek, nie przestawał wzdychać.
«Cóż dziwnego — rzekł Hrabia — koszt wielki, a nuda
Jeszcze większa; chcę skończyć, lecz szlachcic maruda
Upiera się; przewidział, że mię znudzić może:
Dłużej też nie wytrzymam i dzisiaj broń złożę,
Przyjmę warunki zgody, jakie mi sąd poda…» 
«Zgody? — krzyknął Gerwazy — z Soplicami zgoda?
Z Soplicami, mopanku?» — To mówiąc wykrzywił
Usta, jakby nad własną mową się zadziwił.
«Zgoda i Soplicowie! Mopanku, panisko,
Pan żartuje, co? Zamek, Horeszków siedlisko,
Ma pójść w ręce Sopliców? Niech pan tylko raczy
Zsiąść z konia. Pójdźmy w zamek. Niech no pan obaczy.
Pan sam nie wie, co robi. Niech się pan nie wzbrania,
Zsiadaj pan» — i przytrzymał strzemię do zsiadania.
Weszli w zamek; Gerwazy stanął w progu sieni:
«Tu — rzekł — dawni panowie dworem otoczeni,
Często siadali w krzesłach w poobiedniej porze.
Pan godził spory włościan lub w dobrym humorze
Gościom różne ciekawe historyje prawił,
Albo ich powieściami i żarty się bawił,
A młodzież na dziedzińcu biła się w palcaty,
Lub ujeżdżała pańskie tureckie bachmaty». 
Weszli w sień. Rzekł Gerwazy: «W tej ogromnej sieni
Brukowanej nie znajdziesz pan tyle kamieni,
Ile tu pękło beczek wina w dobrych czasach;
Szlachta ciągnęła kufy z piwnicy na pasach,
Sproszona na sejm albo sejmik powiatowy,
Albo na imieniny pańskie, lub na łowy.
Podczas uczty na chorze tym kapela stała,
I w organ, i w rozliczne instrumenty grała;
A gdy wnoszono zdrowie, trąby jak w dniu sądnym
Grzmiały z choru; wiwaty szły ciągiem porządnym:
Pierwszy wiwat za zdrowie Króla Jegomości,
Potem prymasa, potem Królowej Jejmości,
Potem szlachty i całej Rzeczypospolitej,
A na koniec po piątej szklanicy wypitej,
Wnoszono: »Kochajmy się«. Wiwat bez przestanku,
Który dniem okrzykniony, brzmiał aż do poranku;
A już gotowe stały cugi i podwody,
Aby każdego odwieźć do jego gospody». 
Przeszli już kilka komnat. Gerwazy w milczeniu,
Tu wzrok na ścianie wstrzymał, ówdzie na sklepieniu,
Przywołując pamiątkę tu smutną, tam miłą;
Czasem, jakby chciał mówić: «Wszystko się skończyło»,
Kiwnął żałośnie głową; czasem machnął ręką:
Widać, że mu wspomnienie samo było męką,
I że je chciał odpędzić. Aż się zatrzymali
Na górze, w wielkiej, niegdyś zwierciadlanej sali.
Dziś wydartych zwierciadeł stały puste ramy,
Okna bez szyb, z krużgankiem wprost naprzeciw bramy.
Tu wszedłszy, starzec głowę zadumaną skłonił
I twarz zakrył rękami; a gdy ją odsłonił,
Miała wyraz żałości wielkiej i rozpaczy.
Hrabia, chociaż nie wiedział, co to wszystko znaczy,
Poglądając w twarz starca czuł jakieś wzruszenie,
Rękę mu ścisnął; chwilę trwało to milczenie,
Przerwał je starzec, trzęsąc wzniesioną prawicą:
«Nie masz zgody, mopanku, pomiędzy Soplicą
I krwią Horeszków; w panu krew Horeszków płynie,
Jesteś krewnym Stolnika, po matce łowczynie,
Która się rodzi z drugiej córki kasztelana,
Który był, jak wiadomo, wujem mego pana.
Słuchaj pan historyi swej własnej rodzinnej,
Która się stała właśnie w tej izbie, nie innej.
Nieboszczyk pan mój, Stolnik, pierwszy pan w powiecie,
Bogacz i familiant, miał jedyne dziecię,
Córkę piękną jak anioł; więc się zalecało
Stolnikównie i szlachty, i paniąt niemało.
Między szlachtą był jeden wielki paliwoda,
Kłótnik, Jacek Soplica, zwany Wojewoda
Przez żart; w istocie wiele znaczył w województwie,
Bo rodzinę Sopliców miał jakby w dowództwie,
I trzystu ich kreskami rządził wedle woli,
Choć sam nic nie posiadał prócz kawałka roli,
Szabli i wielkich wąsów od ucha do ucha.
Owoż pan Stolnik nieraz wzywał tego zucha,
I ugaszczał w pałacu, zwłaszcza w czas sejmików,
Popularny dla jego krewnych i stronników.
Wąsal tak wzbił się w dumę łaskawym przyjęciem,
Że mu się uroiło zostać pańskim zięciem.
Do zamku nieproszony coraz częściej jeździł,
W końcu u nas jak w swoim domu się zagnieździł.
I już miał się oświadczać: lecz pomiarkowano,
I czarną mu polewkę do stołu podano.
Podobno Stolnikównie wpadł Soplica w oko,
Ale przed rodzicami taiła głęboko.
Było to za Kościuszki czasów; pan popierał
Prawo trzeciego maja i już szlachtę zbierał,
Aby konfederatom ciągnąć ku pomocy,
Gdy nagle Moskwa zamek opasała w nocy.
Ledwie był czas z moździerza na trwogę wypalić,
Podwoje dolne zamknąć i ryglem zawalić.
W zamku całym był tylko: pan Stolnik, ja, pani,
Kuchmistrz i dwóch kuchcików, wszyscy trzej pijani,
Proboszcz, lokaj, hajducy czterej, ludzie śmiali.
Więc za strzelby, do okien. Aż tu tłum Moskali,
Krzycząc: »Ura!«, od bramy wali po tarasie;
My im ze strzelb dziesięciu palnęli »A zasie«.
Nic tam nie było widać; słudzy bez ustanku
Strzelali z dolnych pięter, a ja i pan z ganku.
Wszystko szło pięknym ładem, choć w tak wielkiej trwodze:
Dwadzieścia strzelb leżało tu na tej podłodze;
Wystrzeliliśmy jedną, podawano drugą.
Ksiądz proboszcz zatrudniał się czynnie tą usługą,
I pani, i panienka, i nadworne panny:
Trzech było strzelców, a szedł ogień nieustanny.
Grad kul sypały z dołu moskiewskie piechury;
My z rzadka, ale celniej dogrzewali z góry.
Trzy razy aż pode drzwi to chłopstwo się wparło,
Ale za każdym razem trzech nogi zadarło,
Więc uciekli pod lamus; a już był poranek.
Pan Stolnik wesół wyszedł ze strzelbą na ganek,
I skoro spod lamusa Moskal łeb wychylił,
On dawał zaraz ognia, a nigdy nie mylił;
Za każdym razem czarny kaszkiet w trawę padał
I już się rzadko który zza ściany wykradał.
Stolnik, widząc strwożone swe nieprzyjaciele,
Myślił zrobić wycieczkę, porwał karabelę 
I z ganku krzycząc sługom wydawał rozkazy;
Obróciwszy się do mnie, rzekł: »Za mną Gerwazy!«
Wtem strzelono spod bramy… Stolnik się zająknął,
Zaczerwienił się, zbladnął, chciał mówić, krwią chrząknął:
Postrzegłem wtenczas kulę, wpadła w piersi same.
Pan słaniając się, palcem ukazał na bramę:
Poznałem tego łotra Soplicę! poznałem!
Po wzroście i po wąsach! Jego to postrzałem
Zginął Stolnik, widziałem! Łotr jeszcze do góry
Wzniesioną trzymał strzelbę, jeszcze dym szedł z rury!
Wziąłem go na cel; zbójca stał jak skamieniały!
Dwa razy dałem ognia, i oba wystrzały
Chybiły: czym ze złości, czy z żalu źle mierzył…
Usłyszałem wrzask kobiet, spojrzałem — pan nie żył».
Tu Gerwazy umilknął i łzami się zalał,
Potem rzekł kończąc: «Moskal już wrota wywalał:
Bo po śmierci Stolnika stałem bezprzytomnie,
I nie widziałem, co się działo wokoło mnie.
Szczęściem, na odsiecz przyszedł nam Parafianowicz,
Przywiódłszy Mickiewiczów dwiestu z Horbatowicz,
Którzy są szlachta liczna i dzielna, człek w człeka,
A nienawidzą rodu Sopliców od wieka. 
Tak zginął pan potężny, pobożny i prawy,
Który miał w domu krzesła, wstęgi i buławy,
Ojciec włościan, brat szlachty; i nie miał po sobie
Syna, który by zemstę poprzysiągł na grobie!
Ale miał sługi wierne. Ja w krew jego rany
Obmoczyłem mój rapier Scyzorykiem zwany
(Zapewne pan o moim słyszał Scyzoryku,
Sławnym na każdym sejmie, targu i sejmiku).
Przysiągłem wyszczerbić go na Sopliców karkach,
Ścigałem ich na sejmach, zajazdach, jarmarkach.
Dwóch zarąbałem w kłótni, dwóch na pojedynku;
Jednego podpaliłem w drewnianym budynku,
Kiedyśmy zajeżdżali z Rymszą Korelicze:
Upiekł się tam jak piskorz; a tych nie policzę,
Którym uszy obciąłem. Jeden tylko został,
Który dotąd ode mnie pamiątki nie dostał:
Rodzoniutki braciszek owego wąsala!
Żyje dotąd i z swoich bogactw się przechwala,
Zamku Horeszków tyka swych kopców krawędzią,
Szanowany w powiecie, ma urząd, jest Sędzią!
I pan mu zamek oddasz? Niecne jego nogi
Mają krew pana mego zetrzeć z tej podłogi?
O nie! Póki Gerwazy ma choć za grosz duszy,
I tyle sił, że jednym małym palcem ruszy
Scyzoryk swój wiszący dotychczas na ścianie,
Póty Soplica tego zamku nie dostanie!»
«O! — krzyknął Hrabia, ręce podnosząc do góry —
Dobre miałem przeczucie, żem lubił te mury!
Choć nie wiedziałem, że w nich taki skarb się mieści,
Tyle scen dramatycznych i tyle powieści!
Skoro zamek mych przodków Soplicom zagrabię,
Ciebie osadzę w murach jak mego burgrabię.
Twoja powieść, Gerwazy, zajęła mię mocno.
Szkoda, żeś mię nie przywiódł tu w godzinę nocną;
Udrapowany płaszczem, siadłbym na ruinach,
A ty byś mi o krwawych rozpowiadał czynach.
Szkoda, że masz niewielki dar opowiadania!
Nieraz takie słyszałem i czytam podania;
W Anglii i w Szkocyi każdy zamek lordów,
W Niemczech każdy dwór grafów był teatrem mordów.
W każdej dawnej, szlachetnej, potężnej rodzinie
Jest wieść o jakimś krwawym lub zdradzieckim czynie,
Po którym zemsta spływa na dziedziców w spadku:
W Polsce pierwszy raz słyszę o takim wypadku. 
Czuję, że we mnie mężnych krew Horeszków płynie!
Wiem, co winienem sławie i mojej rodzinie.
Tak, muszę zerwać wszelkie z Soplicą układy,
Choćby do pistoletów przyszło lub do szpady!
Honor każe». Rzekł, ruszył uroczystym krokiem,
A Gerwazy szedł z tyłu w milczeniu głębokiem.
Przed bramą stanął Hrabia, sam do siebie gadał,
Poglądając na zamek prędko na koń wsiadał,
Tak samotną rozmowę kończąc roztargniony:
«Szkoda, że ten Soplica stary nie ma żony
Lub córki pięknej, której ubóstwiałbym wdzięki!
Kochając i nie mogąc otrzymać jej ręki,
Nowa by się w powieści zrobiła zawiłość:
Tu serce, tam powinność — tu zemsta, tam miłość!»
Tak szepcąc spiął ostrogi; koń leciał do dworu,
Gdy z drugiej strony strzelcy wyjeżdżali z boru.
Hrabia lubił myślistwo, ledwie strzelców zoczył,
Zapomniawszy o wszystkim, prosto ku nim skoczył,
Mijając bramę, ogród, płoty: gdy w zawrocie
Obejrzał się, i konia zatrzymał przy płocie. 
Był sad. —
Drzewa owocne, zasadzone w rzędy,
Ocieniały szerokie pole; spodem grzędy.
Tu kapusta, sędziwe schylając łysiny,
Siedzi i zda się dumać o losach jarzyny;
Tam, plącząc stronki w marchwi zielonej warkoczu,
Wysmukły bób obraca na nią tysiąc oczu;
Owdzie podnosi złotą kitę kukuruza;
Gdzieniegdzie otyłego widać brzuch harbuza,
Który od swej łodygi aż w daleką stronę,
Wtoczył się jak gość między buraki czerwone.
Grzędy rozcięte miedzą; na każdym przykopie 
Stoją jakby na straży w szeregach konopie,
Cyprysy jarzyn; ciche, proste i zielone,
Ich liście i woń służą grzędom za obronę,
Bo przez ich liście nie śmie przecisnąć się żmija,
A ich woń gąsienice i owad zabija. 
Dalej maków białawe górują badyle;
Na nich, myślisz, iż rojem usiadły motyle
Trzepiotąc skrzydełkami, na których się mieni
Z rozmaitością tęczy blask drogich kamieni:
Tylą farb żywych, różnych, mak źrenicę mami.
W środku kwiatów, jak pełnia pomiędzy gwiazdami,
Krągły słonecznik licem wielkim, gorejącem,
Od wschodu do zachodu kręci się za słońcem. 
Pod płotem wąskie, długie, wypukłe pagórki,
Bez drzew, krzewów i kwiatów: ogród na ogórki.
Pięknie wyrosły; liściem wielkim, rozłożystym,
Okryły grzędy jakby kobiercem fałdzistym.
Pośrodku szła dziewczyna w bieliznę ubrana,
W majowej zieloności tonąc po kolana;
Z grzęd zniżając się w bruzdy, zdała się nie stąpać,
Ale pływać po liściach, w ich barwie się kąpać. 
Słomianym kapeluszem osłoniła głowę,
Od skroni powiewały dwie wstążki różowe
I kilka puklów światłych, rozwitych warkoczy;
Na ręku miała koszyk, w dół spuściła oczy,
Prawą rękę podniosła niby do chwytania,
Jako dziewczę, gdy rybki w kąpieli ugania
Bawiące się z jej nóżką, tak ona co chwila
Z rękami i koszykiem po owoc się schyla,
Który stopą nadtrąci lub dostrzeże okiem.
Pan Hrabia zachwycony tak cudnym widokiem
Stał cicho. Słysząc tętent towarzyszów w dali,
Ręką dał znak, ażeby wstrzymać konie; stali.
On patrzył z wyciągniętą szyją, jak dziobaty
Żuraw z dala od stada gdy odprawia czaty,
Stojąc na jednej nodze, z czujnymi oczyma,
I by nie zasnąć, kamień w drugiej nodze trzyma. 
Zbudził Hrabiego szelest na plecach i skroni;
Był to bernardyn, kwestarz Robak, a miał w dłoni
Podniesione do góry węzłowate sznurki:
«Ogórków chcesz Waść — krzyknął — oto masz ogórki!
Wara, panie, od szkody; na tutejszej grzędzie
Nie dla Waszeci owoc, nic z tego nie będzie».
Potem palcem pogroził, kaptura poprawił,
I odszedł. Hrabia jeszcze chwilę w miejscu bawił,
Śmiejąc się i klnąc razem tej nagłej przeszkodzie.
Okiem powrócił w ogród, ale już w ogrodzie
Nie było jej; mignęła tylko śród okienka
Jej różowa wstążeczka i biała sukienka.
Widać na grzędach, jaką przeleciała drogą,
Bo liść zielony, w biegu potrącony nogą,
Podnosił się, drżał chwilę, aż się uspokoił,
Jak woda, którą ptaszek skrzydłami rozkroił.
A na miejscu, gdzie stała, tylko porzucony
Koszyk mały z rokity, denkiem wywrócony,
Pogubiwszy owoce na liściach zawisał,
I wśród fali zielonej jeszcze się kołysał. 
Po chwili wszędzie było samotnie i głucho.
Hrabia oczy w dom utkwił i natężył ucho;
Zawsze dumał, a strzelcy zawsze nieruchomie
Za nim stali. Aż w cichym i samotnym domie 
Wszczął się naprzód szmer, potem gwar i krzyk wesoły
Jak w ulu pustym, kiedy weń wlatują pszczoły.
Był to znak, że wracali goście z polowania,
I krzątała się służba około śniadania. 
Jakoż po wszystkich izbach panował ruch wielki:
Roznoszono potrawy, sztućce i butelki.
Mężczyźni tak jak weszli, w swych zielonych strojach,
Z talerzami, z szklankami, chodząc po pokojach,
Jedli, pili lub wsparci na okien uszakach,
Rozprawiali o flintach, chartach i szarakach.
Podkomorstwo i Sędzia przy stole; a w kątku
Panny szeptały z sobą. Nie było porządku,
Jaki się przy obiadach i wieczerzach chowa;
Była to w staropolskim domu moda nowa:
Przy śniadaniach pan Sędzia, choć nierad, pozwalał
Na taki nieporządek, lecz go nie pochwalał. 
Różne też były dla dam i mężczyzn potrawy:
Tu roznoszono tace z całą służbą kawy,
Tace ogromne, w kwiaty ślicznie malowane,
Na nich kurzące wonnie imbryki blaszane
I z porcelany saskiej złote filiżanki;
Przy każdej garnuszeczek mały do śmietanki.
Takiej kawy, jak w Polszcze, nie ma w żadnym kraju:
W Polszcze, w domu porządnym, z dawnego zwyczaju,
Jest do robienia kawy osobna niewiasta,
Nazywa się kawiarka; ta sprowadza z miasta,
Lub z wicin bierze ziarna w najlepszym gatunku
I zna tajne sposoby gotowania trunku,
Który ma czarność węgla, przejrzystość bursztynu,
Zapach moki i gęstość miodowego płynu.
Wiadomo, czym dla kawy jest dobra śmietana;
Na wsi nietrudno o nią: bo kawiarka z rana,
Przystawiwszy imbryki, odwiedza mleczarnie
I sama lekko świeży nabiału kwiat garnie
Do każdej filiżanki w osobny garnuszek,
Aby każdą z nich ubrać w osobny kożuszek.
Panie starsze, już wcześniej wstawszy, piły kawę;
Teraz drugą dla siebie zrobiły potrawę
Z gorącego, śmietaną bielonego piwa,
W którym twaróg gruzłami posiekany pływa.
Zaś dla mężczyzn wędliny leżą do wyboru:
Półgęski tłuste, kumpie, skrzydliki ozoru,
Wszystkie wyborne, wszystkie sposobem domowym
Uwędzone w kominie dymem jałowcowym;
W końcu wniesiono zrazy na ostatnie danie:
Takie bywało w domu Sędziego śniadanie.
We dwóch izbach dwa różne skupiły się grona:
Starszyzna przy stoliku małym zgromadzona
Mówiła o sposobach nowych gospodarskich,
O nowych coraz sroższych ukazach cesarskich;
Podkomorzy krążące o wojnie pogłoski
Oceniał i wyciągał polityczne wnioski.
Panna Wojska, włożywszy okulary sine,
Zabawiała kabałą z kart Podkomorzynę.
W drugiej izbie toczyła młodzież rzecz o łowach
W spokojniejszych i cichszych niż zwykle rozmowach:
Bo Asesor i Rejent, oba mówcy wielcy,
Pierwsi znawcy myślistwa i najlepsi strzelcy,
Siedzieli przeciw sobie mrukliwi i gniewni.
Oba dobrze poszczuli, oba byli pewni
Zwycięstwa swoich chartów: gdy pośród równiny
Znalazł się zagon chłopskiej niezżętej jarzyny.
Tam wpadł zając; już Kusy, już go Sokół imał,
Gdy Sędzia dojeżdżaczy na miedzy zatrzymał.
Musieli być posłuszni, chociaż w wielkim gniewie;
Psy powróciły same i nikt pewnie nie wie,
Czy zwierz uszedł, czy wzięty; nikt zgadnąć nie zdoła,
Czy wpadł w paszczę Kusego, czyli też Sokoła,
Czyli obydwu razem: różnie sądzą strony,
I spór na dalsze czasy trwał nierozstrzygniony. 
Wojski stary od izby do izby przechodził,
Po obu stronach oczy roztargnione wodził,
Nie mieszał się w myśliwych ni w starców rozmowę
I widać, że czym innym zajętą miał głowę.
Nosił skórzaną plackę: czasem w miejscu stanie,
Duma długo i — muchę zabije na ścianie.
Tadeusz z Telimeną, pomiędzy izbami
Stojąc we drzwiach na progu, rozmawiali sami.
Niewielki oddzielał ich od słuchaczów przedział,
Więc szeptali. Tadeusz teraz się dowiedział:
Że ciocia Telimena jest bogata pani,
Że nie są kanonicznie z sobą powiązani
Zbyt bliskim pokrewieństwem; i nawet niepewno,
Czy ciocia Telimena jest synowca krewną,
Choć ją stryj zowie siostrą, bo wspólni rodzice
Tak ich kiedyś nazwali mimo lat różnicę;
Że potem ona żyjąc w stolicy czas długi
Wyrządziła niezmierne Sędziemu usługi;
Stąd ją Sędzia szanował bardzo i przed światem
Lubił, może z próżności, nazywać się bratem,
Czego mu Telimena przez przyjaźń nie wzbrania.
Ulżyły Tadeusza sercu te wyznania.
Wiele też innych rzeczy sobie oświadczyli;
A wszystko to się stało w jednej krótkiej chwili. 
Ale w izbie na prawo, kusząc Asesora,
Rzekł Rejent mimojazdem: «Ja mówiłem wczora,
Że polowanie nasze udać się nie może:
Jeszcze zbyt wcześnie, jeszcze na pniu stoi zboże
I mnóstwo sznurów chłopskiej niezżętej jarzyny:
Stąd i Hrabia nie przybył mimo zaprosiny.
Hrabia na polowaniu bardzo dobrze zna się,
Nieraz gadał o łowów i miejscu, i czasie;
Hrabia chował się w obcych krajach od dzieciństwa
I powiada, że to jest znakiem barbarzyństwa
Polować, tak jak u nas, bez żadnego względu
Na artykuły ustaw, przepisy urzędu,
Nie szanując niczyich kopców ani miedzy,
Jeździć po cudzym gruncie, bez dziedzica wiedzy,
Wiosną równie jak latem zbiegać pola, knieje,
Zabijać nieraz lisa, właśnie gdy linieje,
Albo cierpieć, iż kotną samicę zajęczą
Charty w runi uszczują, a raczej zamęczą,
Z wielką szkodą zwierzyny. Stąd się Hrabia żali,
Że cywilizacyja większa u Moskali;
Bo tam o polowaniu są ukazy cara
I dozór policyi, i na winnych kara». 
Telimena ku lewej izbie obrócona
Wachlując batystową chusteczką ramiona:
«Jak mamę kocham — rzekła — Hrabia się nie myli.
Znam ja dobrze Rosyją. Państwo nie wierzyli,
Gdy im nieraz mówiłam, jak tam z wielu względów
Godna pochwały czujność i srogość urzędów.
Byłam ja w Petersburku, nie raz, nie dwa razy!
Miłe wspomnienia! wdzięczne przeszłości obrazy!
Co za miasto! Nikt z panów nie był w Petersburku?
Chcecie może plan widzieć? Mam plan miasta w biurku.
Latem świat petersburski zwykł mieszkać na daczy,
To jest w pałacach wiejskich (dacza wioskę znaczy).
Mieszkałam w pałacyku, tuż nad Newą rzeką,
Niezbyt blisko od miasta i niezbyt daleko,
Na niewielkim, umyślnie sypanym pagórku:
Ach, co to był za domek! Plan mam dotąd w biurku.
Otóż, na me nieszczęście, najął dom w sąsiedztwie
Jakiś mały czynownik siedzący na śledztwie;
Trzymał kilkoro chartów: co to za męczarnie,
Gdy blisko mieszka mały czynownik i psiarnie!
Ilekroć z książką wyszłam sobie do ogrodu,
Użyć księżyca blasku, wieczornego chłodu
Zaraz i pies przyleciał, i kręcił ogonem,
I strzygł uszami, właśnie jakby był szalonym.
Nieraz się nalękałam. Serce mi wróżyło
Z tych psów jakieś nieszczęście: tak się też zdarzyło.
Bo gdym szła do ogrodu pewnego poranka,
Chart u nóg mych zadławił mojego kochanka
Bonończyka! Ach, była to rozkoszna psina,
Miałam ją w podarunku od księcia Sukina
Na pamiątkę; rozumna, żywa jak wiewiórka:
Mam jej portrecik, tylko nie chcę iść do biurka.
Widząc ją zadławioną, z wielkiej alteracji 
Dostałam mdłości, spazmów, serca palpitacji.
Może by gorzej jeszcze z moim zdrowiem było;
Szczęściem, nadjechał właśnie z wizytą Kiryło
Gawrylicz Kozodusin, wielki łowczy dworu.
Pyta się o przyczynę tak złego humoru,
Każe wnet urzędnika przyciągnąć za uszy;
Staje pobladły, drżący i prawie bez duszy.
»Jak śmiesz — krzyknął Kiryło piorunowym głosem —
Szczuć wiosną łanię kotną tuż pod carskim nosem?«
Osłupiały czynownik darmo się zaklinał,
Że polowania dotąd jeszcze nie zaczynał,
Że z wielkiego łowczego wielkim pozwoleniem,
Zwierz uszczuty zda mu się być psem, nie jeleniem.
»Jak to? — krzyknął Kiryło — to śmiałbyś, hultaju,
Znać się lepiej na łowach i zwierząt rodzaju
Niźli ja, Kozodusin, carski jegermajster?
Niechajże nas rozsądzi zaraz policmajster!«
Wołają policmajstra, każą spisać śledztwo.
»Ja — rzecze Kozodusin — wydaję świadectwo,
Że to łania; on plecie, że to pies domowy:
Rozsądź nas, kto zna lepiej zwierzynę i łowy!«
Policmajster powinność służby swej rozumiał:
Bardzo się nad zuchwalstwem czynownika zdumiał
I odwiódłszy na stronę po bratersku radził,
By przyznał się do winy i tym grzech swój zgładził.
Łowczy udobruchany przyrzekł, że się wstawi
Do cesarza i wyrok nieco ułaskawi.
Skończyło się, że charty poszły na powrozy,
A czynownik na cztery tygodnie do kozy.
Zabawiła nas cały wieczór ta pustota;
Zrobiła się nazajutrz z tego anegdota,
Że w sądy o mym piesku wielki łowczy wdał się:
I nawet wiem z pewnością, że sam cesarz śmiał się».
Śmiech powstał w obu izbach. Sędzia z bernardynem
Grał w mariasza i właśnie z wyświeconym winem
Miał coś ważnego zadać: już ksiądz ledwo dyszał,
Kiedy Sędzia początek powieści posłyszał
I tak nią był zajęty, że z zadartą głową,
I z kartą podniesioną, do bicia gotową,
Siedział cicho i tylko bernardyna trwożył.
Aż gdy skończono powieść, pamfila położył,
I rzekł śmiejąc się: «Niech tam sobie kto chce chwali
Niemców cywilizcją, porządek Moskali;
Niechaj Wielkopolanie uczą się od Szwabów
Prawować się o lisa i przyzywać drabów,
By wziąć w areszt ogara, że wpadł w cudze gaje:
Na Litwie, chwała Bogu, stare obyczaje.
Mamy dosyć zwierzyny dla nas i sąsiedztwa,
I nie będziemy nigdy o to robić śledztwa;
I zboża mamy dosyć, psy nas nie ogłodzą,
Że po jarzynach albo po życie pochodzą:
Na morgach chłopskich bronię robić polowanie». 
Ekonom z lewej izby rzekł: «Nie dziw, mospanie,
Bo też pan tak drogo płaci za taką zwierzynę.
Chłopy i radzi temu, kiedy w ich jarzynę
Wskoczy chart; niech otrząśnie dziesięć kłosów żyta:
To pan mu kopę oddasz i jeszcze nie kwita:
Często chłopi talara w przydatku dostali.
Wierz mi pan, że się chłopstwo bardzo rozzuchwali,
Jeśli…» — Reszty dowodów pana Ekonoma
Nie mógł usłyszeć Sędzia; bo pomiędzy dwoma
Rozprawami, wszczęło się dziesięć rozgoworów,
Anegdot, opowiadań i na koniec sporów. 
Tadeusz z Telimeną, całkiem zapomniani,
Pamiętali o sobie. Rada była pani,
Że jej dowcip tak bardzo Tadeusza bawił;
Młodzieniec jej nawzajem komplementy prawił.
Telimena mówiła coraz wolniej, ciszéj,
I Tadeusz udawał, że jej nie dosłyszy
W tłumie rozmów: więc szepcąc tak zbliżył się do niéj,
Że uczuł twarzą lubą gorącość jej skroni;
Wstrzymując oddech, usty chwytał jej westchnienie
I okiem łowił wszystkie jej wzroku promienie.
Wtem pomiędzy ich usta mignęła znienacka
Naprzód mucha, a za nią tuż Wojskiego placka.
Na Litwie much dostatek. Jest pomiędzy nimi
Gatunek much osobny, zwanych szlacheckimi.
Barwą i kształtem całkiem podobne do innych,
Ale pierś mają szerszą, brzuch większy od gminnych,
Latając bardzo huczą i nieznośnie brzęczą,
A tak silne, że tkankę przebiją pajęczą,
Lub jeśli która wpadnie, trzy dni będzie bzykać,
Bo z pająkiem sam na sam może się borykać.
Wszystko to Wojski zbadał i jeszcze dowodził,
Że się z tych much szlacheckich pomniejszy lud rodził,
Że one tym są muchom, czym dla roju matki,
Że z ich wybiciem zginą owadów ostatki.
Prawda, że ochmistrzyni ani pleban wioski,
Nie uwierzyli nigdy w te Wojskiego wnioski
I trzymali inaczej o muszym rodzaju;
Lecz Wojski nie odstąpił dawnego zwyczaju:
Ledwo dostrzegł takową muchę, wnet ją gonił.
Właśnie mu teraz szlachcic nad uchem zadzwonił;
Po dwakroć Wojski machnął, zdziwił się, że chybił,
Trzeci raz machnął, tylko co okna nie wybił;
Aż mucha, odurzona od tyla łoskotu,
Widząc dwóch ludzi w progu broniących odwrotu,
Rzuciła się z rozpaczą pomiędzy ich lica;
I tam za nią mignęła Wojskiego prawica.
Raz tak był tęgi, że dwie odskoczyły głowy,
Jak rozdarte piorunem dwie drzewa połowy;
Uderzyły się mocno oboje w uszaki,
Tak, że obojgu sine zostały się znaki.
Szczęściem, nikt nie uważał; bo dotychczasowa
Żywa, głośna, lecz dosyć porządna rozmowa
Zakończyła się nagłym wybuchem hałasu.
Jak strzelcy, gdy na lisa zaciągną do lasu,
Słychać gdzieniegdzie trzask drzew, strzały, psiarni granie,
A wtem dojeżdżacz dzika ruszył niespodzianie,
Dał znak i wrzask powstaje w strzelców i psów tłuszczy,
Jak gdyby się ozwały wszystkie drzewa puszczy:
Tak dzieje się z rozmową. Z wolna się pomyka:
Aż natrafi na przedmiot wielki, jak na dzika.
Dzikiem rozmów strzeleckich, był ów spór zażarty
Rejenta z Asesorem o sławne ich charty.
Krótko trwał, lecz zrobili wiele w jedną chwilę;
Bo razem wyrzucili słów i obelg tyle,
Że wyczerpnęli sporu zwyczajne trzy części,
Przycinki, gniew, wyzwanie — i szło już do pięści. 
Więc ku nim z drugiej izby wszyscy się porwali,
I tocząc się przeze drzwi na kształt bystrej fali,
Unieśli młodą parę stojącą na progu,
Podobną Janusowi, dwulicemu bogu. 
Tadeusz z Telimeną nim na skroniach włosy
Poprawili, już groźne ucichły odgłosy.
Szmer zmieszany ze śmiechem śród ciżby się szerzył;
Nastąpił rozejm kłótni, kwestarz ją uśmierzył:
Człowiek stary, lecz krępy i bardzo pleczysty.
Właśnie kiedy Asesor podbiegł do jurysty,
Gdy już sobie gestami grozili szermierze,
On raptem porwał obu z tyłu za kołnierze
I dwakroć uderzywszy głowy obie mocne
Jedną o drugą, jako jaja wielkanocne,
Rozkrzyżował ramiona na kształt drogowskazu
I we dwa kąty izby rzucił ich od razu.
Chwilę z rozciągnionymi stał w miejscu rękami,
I «Pax, pax, pax vobiscum — krzyczał — pokój z wami!»
Zdziwiły się, zaśmiały nawet strony obie.
Przez szacunek, należny duchownej osobie,
Nie śmiano łajać mnicha; a po takiej probie,
Nikt też nie miał ochoty zaczynać z nim zwadę,
Zaś kwestarz Robak, skoro uciszył gromadę,
Widać było, że wcale tryumfu nie szukał,
Ani groził kłótnikom więcej, ani fukał;
Tylko poprawił kaptur, i ręce za pasem
Zatknąwszy, wyszedł cicho z pokoju. 
Tymczasem
Podkomorzy i Sędzia między dwiema strony
Plac zajęli. Pan Wojski, jakby przebudzony
Z głębokiego dumania, w środku się postawił,
Wąsy siwe pokręcił, kapoty poprawił,
Iskrzyły mu się oczy (zawżdy postrzegano
Ten blask niezwykły, kiedy o łowach gadano),
Obiegał zgromadzenie ognistą źrenicą
I gdzie szmer jeszcze słyszał, jak ksiądz kropielnicą,
Tam uciszając machał swą placką ze skóry;
Wreszcie podniósłszy trzonek z powagą do góry,
Jak laskę marszałkowską, nakazał milczenie.
«Uciszcie się! — powtarzał — miejcie też baczenie,
Wy, co jesteście pierwsi myśliwi w powiecie,
Z gorszącej kłótni waszej co będzie? czy wiecie?
Oto młodzież, na której Ojczyzny nadzieje,
Która ma wsławiać nasze ostępy i knieje,
Która niestety, i tak zaniedbuje łowy,
Może do ich wzgardzenia weźmie pochop nowy.
Widząc, że ci, co innym mają dać przykłady,
Z łowów przynoszą tylko poswarki i zwady!
Miejcie też wzgląd powinny dla mych włosów siwych;
Bo znałem większych dawniej niźli wy myśliwych,
A sądziłem ich nieraz sądem polubownym.
Któż był w lasach litewskich Rejtanowi równym?
Czy obławę zaciągnąć, czy spotkać się z zwierzem,
Kto z Białopiotrowiczem porówna się Jerzym?
Gdzie jest dziś taki strzelec jak szlachcic Żegota,
Co kulą z pistoletu w biegu trafiał kota?
Terajewicza znałem, co idąc na dziki,
Nie brał nigdy innego oręża prócz piki;
Budrewicza, co chodził z niedźwiedziem w zapasy:
Takich mężów widziały niegdyś nasze lasy!
Jeśli do sporu przyszło, jakże spór godzili?
Oto obrali sędziów i zakład stawili.
Ogiński sto włók lasu raz przegrał o wilka;
Niesiołowskiemu borsuk kosztował wsi kilka!
I wy, panowie, pójdźcie za starych przykładem,
I rozstrzygnijcie spór wasz choć mniejszym zakładem.
Słowo wiatr, w sporach słownych nigdy nie masz końca;
Szkoda ust dłużej suszyć kłótnią o zająca.
Więc polubownych sędziów najpierwej obierzcie,
A co wyrzekną, temu sumiennie zawierzcie.
Ja uproszę Sędziego, ażeby nie bronił
Dojeżdżaczowi, choćby po pszenicy gonił;
I tuszę, że tę łaskę otrzymam od pana».
To wyrzekłszy, Sędziego ścisnął za kolana.
«Konia — zawołał Rejent — stawię konia z rzędem,
I opiszę się jeszcze przed ziemskim urzędem,
Iż ten pierścień Sędziemu w salarijum złożę».
«Ja — rzekł Asesor — stawię me złote obroże,
Jaszczurem wykładane, z kółkami ze złota,
I smycz tkany jedwabny, którego robota
Równie cudna jak kamień, co się na nim świeci.
Chciałem ten sprzęt zostawić w dziedzictwie dla dzieci,
Jeślibym się ożenił: ten sprzęt mnie darował
Książę Dominik, kiedym z nim razem polował
I z marszałkiem Sanguszką księciem, z jenerałem
Mejenem, i gdy wszystkich na charty wyzwałem.
Tam, bezprzykładną w dziejach polowania sztuką,
Uszczułem sześć zajęcy pojedynczą suką.
Polowaliśmy wtenczas na Kupiskim błoniu;
Książę Radziwiłł nie mógł dosiedzieć na koniu:
Zsiadł i, objąwszy sławną mą charcicę Kanię,
Trzykroć jej w samą głowę dał pocałowanie,
A potem trzykroć ręką klasnąwszy po pysku,
Rzekł: »Mianuję cię odtąd księżną na Kupisku«.
Tak Napoleon daje wodzom swoim księstwa
Od miejsc, na których wielkie odnieśli zwycięstwa». 
Telimena, znudzona zbyt długimi swary,
Chciała wyjść na dziedziniec, lecz szukała pary;
Wzięła koszyczek z kołka: «Panowie, jak widzę,
Chcecie zostać w pokoju, ja idę na rydze;
Kto łaska, proszę za mną» — rzekła, koło głowy
Obwijając czerwony szal kaszemirowy;
Córeczkę Podkomorstwa wzięła w jedną rękę,
A drugą podchyliła do kostek sukienkę.
Tadeusz milczkiem za nią na grzyby pośpieszył.
Zamiar przechadzki bardzo Sędziego ucieszył;
Widział sposób rozjęcia krzykliwego sporu,
A więc krzyknął: «Panowie, po grzyby do boru!
Kto z najpiękniejszym rydzem do stołu przybędzie,
Ten obok najpiękniejszej panienki usiędzie:
Sam ją sobie wybierze. Jeśli znajdzie dama,
Najpiękniejszego chłopca weźmie sobie sama».
Księga trzecia
Umizgi
Wyprawa Hrabiego na sad — Tajemnicza nimfa gęsi pasie — Podobieństwo grzybobrania do przechadzki cieniów elizejskich — Gatunki grzybów — Telimena w świątyni dumania — Narady tyczące się postanowienia Tadeusza — Hrabia pejzażysta — Tadeusza uwagi malarskie nad drzewami i obłokami — Hrabiego myśl o sztuce — Dzwon — Bilecik — Niedźwiedź, mospanie!

Hrabia wracał do siebie; lecz konia wstrzymywał,
Głową coraz w tył kręcił, w ogród się wpatrywał.
I raz mu się zdawało, że znowu z okienka
Błysnęła tajemnicza, bieluchna sukienka
I coś lekkiego znowu upadło z wysoka,
I przeleciawszy cały ogród w mgnieniu oka,
Pomiędzy zielonymi świeciło ogórki:
Jako promień słoneczny, wykradłszy się z chmurki,
Kiedy śród roli padnie na krzemienia skibę
Lub śród zielonej łąki w drobną wody szybę.
Hrabia zsiadł z konia, sługi odprawił do domu,
A sam ku ogrodowi ruszył po kryjomu.
Dobiegł wkrótce parkanu, znalazł w nim otwory
I wcisnął się po cichu, jak wilk do obory.
Nieszczęściem, trącił krzaki suchego agrestu:
Ogrodniczka, jak gdyby zlękła się szelestu,
Oglądała się wkoło, lecz nic nie spostrzegła;
Przecież ku drugiej stronie ogrodu pobiegła.
A Hrabia bokiem, między wielkie końskie szczawie,
Między liście łopuchu, na rękach, po trawie,
Skacząc jak żaba, cicho przyczołgał się blisko,
Wytknął głowę i ujrzał cudne widowisko. 
W tej części sadu rosły tu i ówdzie wiśnie,
Śród nich zboże w gatunkach zmieszanych umyślnie:
Pszenica, kukuruza, bób, jęczmień wąsaty,
Proso, groszek, a nawet krzewiny i kwiaty.
Domowemu to ptactwu taki ochmistrzyni 
Wymyśliła ogródek: sławna gospodyni,
Zwała się Kokosznicka, z domu Jendykowi-
czówna. Jej wynalazek epokę stanowi
W domowym gospodarstwie; dziś powszechnie znany,
Lecz w owych czasach jeszcze za nowość podany,
Przyjęty pod sekretem od niewielu osób,
Nim go wydał kalendarz, pod tytułem: Sposób 
Na jastrzębie i kanie, albo nowy środek
Wychowywania drobiu — był to ów ogrodek.
Jakoż, zaledwie kogut, co odprawia warty,
Stanie i nieruchomie dzierżąc dziób zadarty,
I głowę grzebieniastą pochyliwszy bokiem,
Aby tym łacniej w niebo mógł celować okiem,
Dostrzeże wiszącego jastrzębia śród chmury,
Krzyknie: zaraz w ten ogród chowają się kury,
Nawet gęsi i pawie, i w nagłym przestrachu
Gołębie, gdy nie mogą schronić się na dachu.
Teraz w niebie żadnego nie widziano wroga;
Tylko skwarzyła słońca letniego pożoga.
Od niej ptaki w zbożowym ukryły się lasku;
Tamte leżą w murawie, te kąpią się w piasku. 
Śród ptaszych głów sterczały główki ludzkie małe,
Odkryte; włosy na nich krótkie, jak len białe;
Szyje nagie do ramion; a pomiędzy nimi
Dziewczyna głową wyższa, z włosami dłuższymi.
Tuż za dziećmi paw siedział i piór swych obręcze
Szeroko rozprzestrzenił w różnofarbną tęczę,
Na której główki białe, jak na tle obrazku,
Rzucone w ciemny błękit, nabierały blasku.
Obrysowane wkoło kręgiem pawich oczu
Jak wiankiem gwiazd, świeciły w zbożu jak w przezroczu,
Pomiędzy kukuruzy złocistymi laski,
I angielską trawicą posrebrzaną w paski,
I szczyrem koralowym, i zielonym ślazem;
Których kształty i barwy mieszały się razem
Niby krata ze srebra i złota pleciona,
A powiewna od wiatru jak lekka zasłona.
Nad gęstwą różnofarbnych kłosów i badylów
Wisiała jak baldachim jasna mgła motylów,
Zwanych babkami, których poczwórne skrzydełka
Lekkie jak pajęczyna, przejrzyste jak szkiełka,
Gdy w powietrzu zawisną, zaledwo widome,
I chociaż brzęczą, myślisz, że są nieruchome.
Dziewczyna powiewała podniesioną w ręku
Szarą kitką, podobną do piór strusich pęku;
Nią zdała się oganiać główki niemowlęce
Od złotego motylów deszczu. W drugiej ręce
Coś u niej rogatego, złocistego świeci,
Zdaje się, że naczynie do karmienia dzieci:
Bo je zbliżała dzieciom do ust po kolei;
Miało zaś kształt złotego rogu Amaltei.
Tak zatrudniona, przecież obracała głowę
Na pamiętne szelestem krzaki agrestowe,
Nie wiedząc, że napastnik już z przeciwnej strony
Przybliżył się, czołgając jak wąż przez zagony,
Aż wyskoczył z łopuchu. Spojrzała — stał blisko,
O cztery grzędy od niej, i kłaniał się nisko.
Już głowę odwróciła i wzniosła ramiona,
I zrywała się lecieć jak kraska spłoszona,
I już lekkie jej stopy wionęły nad liściem,
Kiedy dzieci, przelękłe podróżnego wniściem 
I ucieczką dziewczyny, wrzasnęły okropnie.
Posłyszała, uczuła, że jest nieroztropnie
Dziatwę małą, przelękłą i samą porzucić:
Wracała, wstrzymując się, lecz musiała wrócić,
Jak niechętny duch, wróżka przyzwany zaklęciem,
Przybiegła z najkrzykliwszym bawić się dziecięciem,
Siadła przy nim na ziemi, wzięła je na łono;
Drugie głaskała ręką i mową pieszczoną;
Aż się uspokoiły, objąwszy w rączęta
Jej kolana i tuląc główki jak pisklęta
pod skrzydło matki. Ona rzekła: «Czy to pięknie
Tak krzyczeć? Czy to grzecznie? Ten pan się zalęknie.
Ten pan nie przyszedł straszyć; to nie dziad szkaradny,
To gość, dobry pan, patrzcie tylko jaki ładny». 
Sama spojrzała: Hrabia uśmiechnął się mile,
I widocznie był wdzięczny jej za pochwał tyle;
Postrzegła się, umilkła, oczy opuściła
I jako róży pączek cała się spłoniła.
W istocie był to piękny pan: słusznej urody,
Twarz miał pociągłą, blade lecz świeże jagody,
Oczy modre, łagodne, włos długi, białawy;
Na włosach listki ziela i kosmyki trawy,
Które Hrabia oberwał pełznąc przez zagony,
Zieleniły się jako wieniec rozpleciony. 
«O ty — rzekł — jakimkolwiek uczczę cię imieniem,
Bóstwem jesteś czy nimfą, duchem czy widzeniem!
Mów: własna li cię wola na ziemię sprowadza,
Obca li więzi ciebie na padole władza?
Ach, domyślam się, — pewnie wzgardzony miłośnik,
Jaki pan możny, albo opiekun zazdrośnik,
W tym cię parku zamkowym jak zaklętą strzeże!
Godna, by o cię bronią walczyli rycerze,
Byś została romansów heroiną smutnych!
Odkryj mi, piękna, tajnie twych losów okrutnych!
Znajdziesz wybawiciela. Odtąd twym skinieniem,
Jak rządzisz sercem moim, tak rządź mym ramieniem».
Wyciągnął ramię.
Ona z rumieńcem dziewiczym,
Ale z rozweselonym słuchała obliczem.
Jak dziecię lubi widzieć obrazki jaskrawe
I w liczmanach błyszczących znajduje zabawę,
Nim rozezna ich wartość: tak się słuch jej pieści
Z dźwięcznymi słowy, których nie pojęła treści. 
Na koniec zapytała: «Skąd tu pan przychodzi?
I czego tu po grzędach szuka pan dobrodziéj?»
Hrabia oczy roztworzył. Zmieszany, zdziwiony,
Milczał; wreszcie, zniżając swej rozmowy tony:
«Przepraszam — rzekł — panienko! Widzę, żem pomieszał
Zabawy! Ach, przepraszam: jam właśnie pośpieszał
Na śniadanie: już późno, chciałem na czas zdążyć;
Panienka wie, że drogą trzeba wkoło krążyć,
Przez ogród zdaje mi się jest do dworu prościéj».
Dziewczyna rzekła: «Tędy droga jegomości;
Tylko grząd psuć nie trzeba. Tam, między murawą
Ścieżka». — «W lewo — zapytał Hrabia — czy na prawo?»
Ogrodniczka, podniósłszy błękitne oczęta,
Zdawała się go badać ciekawością zdjęta:
Bo dom o tysiąc kroków widny jak na dłoni,
A Hrabia drogi pyta? Ale Hrabia do niéj
Chciał koniecznie coś mówić i szukał powodu
Rozmowy: «Panna mieszka tu? blisko ogrodu?
Czy na wsi? Jak to było, żem panny we dworze
Nie widział? czy niedawno tu? przyjezdna może?»
Dziewczę wstrząsnęło głową. — «Przepraszam, panienko,
Czy nie tam pokój panny, gdzie owe okienko?»
Myślił zaś w duchu: jeśli nie jest heroiną
Romansów, jest młodziuchną, prześliczną dziewczyną.
Zbyt często wielka dusza, myśl wielka ukryta
W samotności, jak róża śród lasów rozkwita;
Dosyć ją wynieść na świat, postawić przed słońcem,
Aby widzów zdziwiła jasnych barw tysiącem! 
Ogrodniczka tymczasem powstała w milczeniu,
Podniosła jedno dziecię zwisłe na ramieniu,
Drugie wzięła za rękę, a kilkoro przodem
Zaganiając jak gąski, szła dalej ogrodem. 
Odwróciwszy się rzekła: «Czy też pan nie może
Rozbiegłe moje ptastwo wpędzić nazad w zboże?»
«Ja, ptastwo pędzać?» krzyknął Hrabia z zadziwieniem;
Ona tymczasem znikła, zakryta drzew cieniem.
Chwilę jeszcze z szpaleru, przez majowe zwoje,
Przeświecało coś na wskroś jakby oczu dwoje.
Samotny Hrabia długo jeszcze stał w ogrodzie.
Dusza jego, jak ziemia po słońca zachodzie,
Ostygała powoli, barwy brała ciemne;
Zaczął marzyć, lecz sny miał bardzo nieprzyjemne.
Zbudził się, sam nie wiedząc, na kogo się gniewał:
Niestety, mało znalazł! nadto się spodziewał!
Bo gdy zagonem pełzał ku owej pasterce,
Paliło mu się w głowie, skakało w nim serce;
Tyle wdzięków w tajemnej nimfie upatrywał,
W tyle ją cudów ubrał, tyle odgadywał!
Wszystko znalazł inaczej: prawda, że twarz ładną,
Kibić miała wysmukłą, ale jak nieskładną!
A owa pulchność liców i rumieńca żywość,
Malująca zbyteczną, prostacką szczęśliwość!
Znak, że myśl jeszcze drzemie, że serce nieczynne!
I owe odpowiedzi, tak wiejskie, tak gminne!
«Po cóż się łudzić — krzyknął — zgaduję po czasie:
Moja nimfa tajemna pono gęsi pasie!» 
Z nimfy zniknieniem, całe czarowne przezrocze
Zmieniło się. Te wstęgi, te kraty urocze
Złote, srebrne: niestety! więc to była słoma? 
Hrabia z załamanymi poglądał rękoma
Na snopek uwiązanej trawami mietlicy,
Którą brał za pęk strusich piór w ręku dziewicy.
Nie zapomniał naczynia: złocista konewka,
Ów rożek Amaltei, była to marchewka!
Widział ją w ustach dziecka pożeraną chciwie:
Więc było po uroku! po czarach! po dziwie! 
Tak chłopiec, kiedy ujrzy cykoryi kwiaty,
Wabiące dłoń miękkimi, lekkimi bławaty,
Chce je pieścić, zbliża się, dmuchnie: i z podmuchem
Cały kwiat na powietrzu rozleci się puchem,
A w ręku widzi tylko badacz zbyt ciekawy
Nagą łodygę szarozielonawej trawy.
Hrabia wcisnął na oczy kapelusz i wracał
Tamtędy, kędy przyszedł; ale drogę skracał,
Stąpając po jarzynach, kwiatach i agreście,
Aż, przeskoczywszy parkan, odetchnął nareście! 
Przypomniał, że dziewczynie mówił o śniadaniu;
Może już wszyscy wiedzą o jego spotkaniu
W ogrodzie, blisko domu? może szukać wyślą?
Postrzegli, że uciekał? kto wie, co pomyślą?
Więc wypadało wrócić. Chyląc się u płotów
Około miedz i zielska, po tysiącach zwrotów
Rad był przecież, że wyszedł w końcu na gościniec,
Który prosto prowadził na dworski dziedziniec.
Szedł przy płocie, a głowę odwracał od sadu.
Jak złodziej od spichlerza, aby nie dać śladu,
Że go myśli nawiedzić albo już nawiedził:
Tak Hrabia był ostrożny, choć go nikt nie śledził;
Patrzył w stronę przeciwną ogrodu, na prawo. 
Był gaj z rzadka zarosły, wysłany murawą.
Po jej kobiercach, na wskroś białych pniów brzozowych,
Pod namiotem obwisłych gałęzi majowych,
Snuło się mnóstwo kształtów, których dziwne ruchy,
Niby tańce, i dziwny ubiór: istne duchy
Błądzące po księżycu. Tamci w czarnych, ciasnych,
Ci w długich, rozpuszczonych szatach jak śnieg jasnych;
Tamten pod kapeluszem jak obręcz szerokim,
Ten z gołą głową; inni jak gdyby obłokiem
Obwiani, idąc, na wiatr puszczają zasłony,
Ciągnące się za głową, jak komet ogony.
Każdy w innej postawie: ten przyrósł do ziemi,
Tylko oczyma kręci na dół spuszczonemi;
Ów, patrząc wprost przed siebie, niby senny kroczy,
Jak po linie, ni w prawo, ni w lewo nie zboczy;
Wszyscy zaś ciągle w różne schylają się strony
Aż do ziemi, jak gdyby wybijać pokłony.
Jeżeli się przybliżą albo się spotkają,
Ani mówią do siebie, ani się witają,
Głęboko zadumani, w sobie pogrążeni.
Hrabia widział w nich obraz elizejskich cieni,
Które, chociaż boleściom, troskom niedostępne,
Błąkają się spokojne, ciche, lecz posępne. 
Któż by zgadnął, że owi tak mało ruchomi,
Owi milczący ludzie — są nasi znajomi,
Sędziowscy towarzysze? Z hucznego śniadania
Wyszli na uroczysty obrzęd grzybobrania. 
Jako ludzie rozsądni, umieją miarkować
Mowy i ruchy swoje, aby je stosować
W każdej okoliczności do miejsca i czasu.
Dlatego, nim ruszyli za Sędzią do lasu,
Wzięli postawy tudzież ubiory odmienne,
Służące do przechadzki opończe płócienne,
Którymi osłaniają po wierzchu kontusze,
A na głowy słomiane wdziali kapelusze.
Stąd biali wyglądają jak czyśćcowe dusze.
Młodzież także przebrana, oprócz Telimeny
I kilku po francusku chodzących. 
Tej sceny
Hrabia nie pojął; nie znał wiejskiego zwyczaju:
Więc zdziwiony niezmiernie biegł pędem do gaju.
Grzybów było w bród. Chłopcy biorą krasnolice,
Tyle w pieśniach litewskich sławione lisice,
Co są godłem panieństwa: bo czerw ich nie zjada,
I dziwna, żaden owad na nich nie usiada.
Panienki za wysmukłym gonią borowikiem,
Którego pieśń nazywa grzybów pułkownikiem.
Wszyscy dybią na rydza; ten wzrostem skromniejszy
I mniej sławny w piosenkach, za to najsmaczniejszy,
Czy świeży, czy solony, czy jesiennej pory,
Czy zimą. Ale Wojski zbierał muchomory. 
Inne pospólstwo grzybów, pogardzone w braku
Dla szkodliwości albo niedobrego smaku,
Lecz nie są bez użytku: one zwierza pasą
I gniazdem są owadów i gajów okrasą.
Na zielonym obrusie łąk, jako szeregi
Naczyń stołowych sterczą: tu z krągłymi brzegi
Surojadki srebrzyste, żółte i czerwone,
Niby czareczki różnym winem napełnione;
Koźlak, jak przewrócone kubka dno wypukłe,
Lejki, jako szampańskie kieliszki wysmukłe,
Bielaki krągłe, białe, szerokie i płaskie,
Jakby mlekiem nalane filiżanki saskie,
I kulista, czarniawym pyłkiem napełniona
Purchawka, jak pieprzniczka; zaś innych imiona,
Znane tylko w zajęczym lub wilczym języku,
Od ludzi nieochrzczone; a jest ich bez liku. 
Ni wilczych, ni zajęczych nikt dotknąć nie raczy;
A kto schyla się ku nim, gdy błąd swój obaczy,
Zagniewany, grzyb złamie albo nogą kopnie:
Tak szpecąc trawę, czyni bardzo nieroztropnie. 
Telimena ni wilczych, ni ludzkich nie zbiera.
Roztargniona, znudzona, dokoła spoziera,
Z głową w górę zadartą. Więc pan Rejent w gniewie
Mówił o niej, że grzybów szukała na drzewie;
Asesor ją złośliwiej równał do samicy,
Która miejsca na gniazdo szuka w okolicy. 
Jakoż zdała się szukać samotności, ciszy.
Oddalała się z wolna od swych towarzyszy,
I szła lasem na wzgórek pochyło wyniosły,
Ocieniony, bo drzewa gęściej na nim rosły.
W środku szarzał się kamień; strumień spod kamienia
Szumiał, tryskał i zaraz, jakby szukał cienia,
Chował się między gęste i wysokie zioła,
Które wodą pojone bujały dokoła;
Tam ów bystry swawolnik, spowijany w trawy
I liściem podesłany, bez ruchu, bez wrzawy,
Niewidzialny i ledwie dosłyszany szepce,
Jako dziecię krzykliwe złożone w kolebce,
Gdy matka nad nim zwiąże firanki majowe
I liścia makowego nasypie pod głowę. 
Miejsce piękne i ciche: tu się często schrania
Telimena, zowiąc je Świątynią dumania. 
Stanąwszy nad strumieniem, rzuciła na trawnik
Z ramion swój szal powiewny, czerwony jak krwawnik;
I podobna pływaczce, która do kąpieli
Zimnej schyla się, nim się zanurzyć ośmieli,
Klęknęła i powoli chyliła się bokiem;
Wreszcie, jakby porwana koralu potokiem,
Upadła nań i cała wzdłuż się rozpostarła.
Łokcie na trawie, skronie na dłoniach oparła,
Z głową na dół skłonioną; na dole u głowy,
Błysnął francuskiej książki papier welinowy;
Nad alabastrowymi stronicami księgi,
Wiły się czarne pukle i różowe wstęgi. 
W szmaragdzie bujnych traw, na krwawnikowym szalu,
W sukni długiej, jak gdyby w powłoce koralu,
Od której odbijał się włos z jednego końca,
Z drugiego czarny trzewik; po bokach błyszcząca
Śnieżną pończoszką, chustką, białością rąk, lica,
Wydawała się z dala jak pstra gąsienica,
Gdy wpełźnie na zielony liść klonu. 
Niestety!
Wszystkie tego obrazu wdzięki i zalety
Darmo czekały znawców, nikt nie zważał na nie,
Tak mocno zajmowało wszystkich grzybobranie. 
Tadeusz przecież zważał i w bok strzelał okiem,
I nie śmiejąc iść prosto, przysuwał się bokiem:
Jak strzelec, gdy w ruchomej gałęzistej szopie,
Usiadłszy na dwóch kołach, podjeżdża na dropie,
Albo na siewki idąc, przy koniu się kryje,
Strzelbę złoży na siodle lub pod końską szyję,
Niby to bronę włóczy, niby jedzie miedzą,
A coraz się przybliża, kędy ptaki siedzą:
Tak skradał się Tadeusz. 
Sędzia czaty zmieszał
I przeciąwszy mu drogę, do źródła pośpieszał.
Z wiatrem igrały białe poły sarafana 
I wielka chustka w pasie końcem uwiązana;
Słomiany, podwiązany kapelusz od ruchu
Nagłego chwiał się z wiatrem jako liść łopuchu,
Spadając to na barki, to znowu na oczy;
W ręku ogromna laska: tak pan Sędzia kroczy.
Schyliwszy się i ręce obmywszy w strumieniu,
Usiadł przed Telimeną na wielkim kamieniu,
I, wsparłszy się oburącz na gałkę słoniową
Trzciny ogromnej, z taką ozwał się przemową:
«Widzi aśćka, od czasu jak tu u nas gości
Tadeuszek, niemało mam niespokojności.
Jestem bezdzietny, stary; ten dobry chłopczyna,
Wszak to moja na świecie pociecha jedyna,
Przyszły dziedzic fortunki mojej. Z łaski nieba,
Zostawię mu kęs niezły szlacheckiego chleba;
Już mu też czas obmyśleć los, postanowienie;
Ale zważaj no, aśćka, moje utrapienie!
Wiesz, że pan Jacek, brat mój, Tadeusza ociec,
Dziwny człowiek, zamiarów jego trudno dociec,
Nie chce wracać do kraju, Bóg wie gdzie się kryje,
Nawet nie chce synowi oznajmić, że żyje,
A ciągle nim zarządza. Naprzód w legijony
Chciał go posyłać; byłem okropnie zmartwiony.
Potem zgodził się przecie, by w domu pozostał
I żeby się ożenił. Jużbyć żony dostał;
Partyję upatrzyłem. Nikt z obywateli
Nie wyrówna z imienia ani z parenteli 
Podkomorzemu; jego starsza córka Anna
Jest na wydaniu, piękna i posażna panna;
Chciałem zagaić». Na to Telimena zbladła,
Złożyła książkę, wstała nieco i usiadła.
«Jak mamę kocham — rzekła — czy to, panie bracie,
Jest w tym sens jaki, czy wy Boga w sercu macie?
To myślisz Tadeusza zostać dobrodziejem,
Jeśli młodego chłopca zrobisz grykosiejem?
Świat mu zawiążesz! wierz mi, kląć was kiedyś będzie!
Zakopać taki talent w lasach i na grzędzie!
Wierz mi, ile poznałam, pojętne to dziecię,
Warto, żeby na wielkim przetarło się świecie.
Dobrze brat zrobi, gdy go do stolicy wyśle,
Na przykład do Warszawy? Lub wie brat, co myślę…
Żeby do Peterburka? Ja pewnie tej zimy
Pojadę tam dla sprawy; razem ułożymy,
Co zrobić z Tadeuszem. Znam tam wiele osób,
Mam wpływy: to najlepszy kreacyi sposób.
Za mą pomocą, znajdzie wstęp w najpierwsze domy,
A kiedy będzie ważnym osobom znajomy,
Dostanie urząd, order; wtenczas niech porzuci
Służbę, jeżeli zechce, niech do domu wróci,
Mając już i znaczenie, i znajomość świata.
I cóż brat myśli o tym?» — «Jużci, w młode lata —
Rzekł Sędzia — nieźle chłopcu trochę się przewietrzyć,
Obejrzeć się na świecie, między ludźmi przetrzéć;
Ja za młodu niemało świata objechałem:
Byłem w Piotrkowie, w Dubnie, to za trybunałem
Jadąc jako palestrant, to własne swe sprawy
Forytując, jeździłem nawet do Warszawy.
Człek niemało skorzystał! Chciałbym i synowca
Wysłać pomiędzy ludzi, prosto jak wędrowca,
Jak czeladnika, który terminuje lata,
Ażeby nabył trochę znajomości świata.
Nie dla rang ni orderów! Proszę uniżenie,
Ranga moskiewska, order: cóż to za znaczenie?
Któryż to z dawnych panów, ba, nawet dzisiejszych,
Między szlachtą w powiecie nieco zamożniejszych,
Dba o podobne fraszki? Przecież są w estymie 
U ludzi; bo szanujem w nich ród, dobre imię,
Albo urząd, lecz ziemski, przyznany wyborem
Obywatelskim, nie zaś czyimś tam faworem».
Telimena przerwała: «Jeśli brat tak myśli,
Tym lepiej, więc go jako wojażera wyślij». 
«Widzi siostra — rzekł Sędzia, skrobiąc smutnie głowę —
Chciałbym bardzo: cóż, kiedy mam trudności nowe!
Pan Jacek nie wypuszcza z opieki swej syna,
I przysłał mi tu właśnie na kark bernardyna
Robaka, który przybył z tamtej strony Wisły,
Przyjaciel brata, wszystkie wie jego zamysły;
A więc o Tadeusza już wyrzekli losie,
I chcą, by się ożenił, aby pojął Zosię,
Wychowankę waćpani. Oboje dostaną,
Oprócz fortunki mojej, z łaski Jacka wiano
W kapitałach; wiesz aśćka, że ma kapitały,
I z łaski jego mam też fundusz prawie cały:
Ma więc prawo rozrządzać… aśćka pomyśl o tem,
Żeby się to zrobiło najmniejszym kłopotem.
Trzeba ich z sobą poznać. Prawda, bardzo młodzi,
Szczególnie Zosia mała, lecz to nic nie szkodzi.
Czas by już Zośkę wreszcie wydobyć z zamknięcia.
Bo wszakci to już pono wyrasta z dziecięcia».
Telimena zdziwiona i prawie wylękła
Podnosiła się coraz, na szalu uklękła;
Zrazu słuchała pilnie, potem dłoni ruchem
Przeczyła, ręką żwawo wstrząsając nad uchem,
Odpędzając jak owad nieprzyjemne słowa
Na powrót w usta mówcy —
«A! a! to rzecz nowa!
Czy to Tadeuszowi szkodzi, czy nie szkodzi —
Rzekła z gniewem — sądź o tym sam waćpan dobrodziéj!
Mnie nic do Tadeusza; sami o nim radźcie,
Zróbcie go ekonomem lub w karczmie posadźcie,
Niech szynkuje lub z lasu niech zwierzynę znosi:
Z nim sobie, co zechcecie, zróbcie. Lecz do Zosi?
Co waćpaństwu do Zosi? Ja jej ręką rządzę,
Ja sama! Że pan Jacek dawał był pieniądze
Na wychowanie Zosi, i że jej wyznaczył
Małą pensyjkę roczną, więcej przyrzec raczył,
Toć jej jeszcze nie kupił. Zresztą, państwo wiecie,
I dotąd jeszcze o tym wiadomo na świecie,
Że hojność państwa dla nas nie jest bez powodu,
Winni coś Soplicowie dla Horeszków rodu».
(Tej części mowy Sędzia słuchał z niepojętem
Pomieszaniem, żałością i widocznym wstrętem;
Jakby lękał się reszty mowy, głowę skłonił,
I ręką potakując, mocno się zapłonił.)
Telimena kończyła: «Byłam jej piastunką,
Jestem krewną, jedyną Zosi opiekunką.
Nikt oprócz mnie nie będzie myślił o jej szczęściu».
«A jeśli ona szczęście znajdzie w tym zamęściu? —
Rzekł Sędzia wzrok podnosząc. — Jeśli Tadeuszka
Podoba?» — «Czy podoba? to na wierzbie gruszka!
Podoba, nie podoba: a to mi rzecz ważna!
Zosia nie będzie, prawda, partyja posażna;
Ale też nie jest z lada wsi, lada szlachcianka,
Idzie z jaśnie wielmożnych, jest wojewodzianka,
Rodzi się z Horeszkówny; małżonka dostanie!
Staraliśmy się tyle o jej wychowanie!
Chybaby tu zdziczała». Sędzia pilnie słuchał,
Patrząc w oczy; zdało się, że się udobruchał,
Bo rzekł dosyć wesoło: «No, to i cóż robić!
Bóg widzi, szczerze chciałem interesu dobić;
Tylko bez gniewu. Jeśli aśćka się nie zgodzi,
Aśćka ma prawo; smutno: gniewać się nie godzi.
Radziłem, bo brat kazał; nikt tu nie przymusza.
Gdy aśćka rekuzuje pana Tadeusza,
Odpisuję Jackowi, że nie z mojej winy
Nie dojdą Tadeusza z Zosią zaręczyny.
Teraz sam będę radzić. Pono z Podkomorzym
Zagaimy swatowstwo i resztę ułożym». 
Przez ten czas Telimena ostygła z zapału:
«Ja nic nie rekuzuję, braciszku, pomału!
Sam mówiłeś, że jeszcze za wcześnie — zbyt młodzi, —
Rozpatrzmy się, czekajmy, nic to nie zaszkodzi,
Poznajmy z sobą państwo młodych, będziem zważać;
Nie można szczęścia drugich tak na traf narażać.
Ostrzegam tylko wcześnie: niech brat Tadeusza
Nie namawia, kochać się w Zosi nie przymusza;
Bo serce nie jest sługa, nie zna co to pany,
I nie da się przemocą okuwać w kajdany».
Za czym Sędzia, powstawszy, odszedł zamyślony.
Pan Tadeusz z przeciwnej przybliżył się strony,
Udając, że szukanie grzybów tam go zwabia.
W tymże kierunku z wolna posuwa się Hrabia.
Hrabia podczas Sędziego sporów z Telimeną
Stał za drzewami, mocno zdziwiony tą sceną.
Dobył z kieszeni papier i ołówek, sprzęty,
Które zawsze miał z sobą, i na pień wygięty,
Rozpiąwszy kartkę, widać, że obraz malował,
Mówiąc sam z sobą: «Jakbyś umyślnie grupował:
Ten na głazie, ta w trawie; grupa malownicza!
Głowy charakterowe! z kontrastem oblicza!»
Podchodził, wstrzymywał się, lornetkę przecierał,
Oczy chustką obwiewał i coraz spozierał:
«Miałożby to cudowne, śliczne widowisko
Zginąć albo zmienić się, gdy podejdę blisko?
Ten aksamit traw, będzież to mak i botwinie?
W nimfie tej czyż obaczę jaką ochmistrzynię?» 
Choć Hrabia Telimenę już dawniej widywał
W domu Sędziego, w którym dosyć często bywał,
Lecz mało ją uważał: zadziwił się zrazu,
Rozeznając w niej model swojego obrazu.
Miejsca piękność, postawy wdzięk i gust ubrania
Zmieniły ją, zaledwo była do poznania.
W oczach świeciły jeszcze niezagasłe gniewy;
Twarz, ożywiona wiatru świeżymi powiewy,
Sporem z Sędzią i nagłym przybyciem młodzieńców,
Nabrała mocnych, żywszych niż zwykle rumieńców. 
«Pani — rzekł Hrabia — racz mej śmiałości darować;
Przychodzę i przepraszać, i razem dziękować.
Przepraszać, że jej kroków śledziłem ukradkiem;
I dziękować, że byłem jej dumania świadkiem.
Tyle ją obraziłem! winienem jej tyle!
Przerwałem chwilę dumań; winienem ci chwile
Natchnienia, chwile błogie! Potępiaj człowieka;
Ale sztukmistrz twojego przebaczenia czeka!
Na wielem się odważył, na więcej odważę:
Sądź!» — tu ukląkł i podał swoje pejzaże.
Telimena sądziła malowania proby
Tonem grzecznej, lecz sztukę znającej osoby;
Skąpa w pochwały, lecz nie szczędziła zachętu:
«Brawo — rzekła — winszuję, niemało talentu.
Tylko pan nie zaniedbuj; szczególniej potrzeba
Szukać pięknej natury! O, szczęśliwe nieba
Krajów włoskich! różowe cezarów ogrody!
Wy, klasyczne Tyburu spadające wody!
I straszne Pauzylipu skaliste wydroże!
To, Hrabio, kraj malarzów! U nas, żal się Boże!…
Dziecko muz, w Soplicowie oddane na mamki,
Umrze pewnie. Mój Hrabio, oprawię to w ramki,
Albo w album umieszczę, do rysunków zbiorku,
Które zewsząd skupiałam: mam ich dosyć w biurku». 
Zaczęli więc rozmowę o niebios błękitach,
Morskich szumach i wiatrach wonnych, i skał szczytach,
Mieszając tu i ówdzie, podróżnych zwyczajem,
Śmiech i urąganie się nad ojczystym krajem. 
A przecież wokoło nich ciągnęły się lasy
Litewskie, tak poważne i tak pełne krasy!
Czeremchy oplatane dzikich chmielów wieńcem,
Jarzębiny ze świeżym pasterskim rumieńcem,
Leszczyna jak menada z zielonymi berły,
Ubranymi jak w grona, w orzechowe perły;
A niżej dziatwa leśna: głóg w objęciu kalin,
Ożyna czarne usta tuląca do malin.
Drzewa i krzewy liśćmi wzięły się za ręce,
Jak do tańca stające panny i młodzieńce
Wkoło pary małżonków. Stoi pośród grona
Para, nad całą leśną gromadą wzniesiona
Wysmukłością kibici i barwy powabem:
Brzoza biała, kochanka, z małżonkiem swym grabem.
A dalej, jakby starce na dzieci i wnuki
Patrzą, siedząc w milczeniu, tu sędziwe buki,
Tam matrony topole i mchami brodaty
Dąb, włożywszy pięć wieków na swój kark garbaty,
Wspiera się, jak na grobów połamanych słupach,
Na dębów, przodków swoich, skamieniałych trupach. 
Pan Tadeusz kręcił się, nudząc niepomału 
Długą rozmową, w której nie mógł brać udziału.
Aż, gdy zaczęto sławić cudzoziemskie gaje,
I wyliczać z kolei wszystkich drzew rodzaje:
Pomarańcze, cyprysy, oliwki, migdały,
Kaktusy, aloesy, mahonie, sandały,
Cytryny, bluszcz, orzechy włoskie, nawet figi,
Wysławiając ich kształty, kwiaty i łodygi:
Tadeusz nie przestawał dąsać się i zżymać,
Na koniec nie mógł dłużej od gniewu wytrzymać.
Był on prostak, lecz umiał czuć wdzięk przyrodzenia,
I patrząc w las ojczysty, rzekł pełen natchnienia:
«Widziałem w botanicznym wileńskim ogrodzie,
Owe sławione drzewa rosnące na wschodzie
I na południu, w owej pięknej włoskiej ziemi;
Któreż równać się może z drzewami naszemi?
Czy aloes z długimi jak konduktor pałki?
Czy cytryna, karlica z złocistymi gałki,
Z liściem lakierowanym, krótka i pękata,
Jako kobieta mała, brzydka, lecz bogata?
Czy zachwalony cyprys długi, cienki, chudy,
Co zdaje się być drzewem nie smutku, lecz nudy?
Mówią, że bardzo smutnie wygląda na grobie;
Jest to jak lokaj Niemiec we dworskiej żałobie,
Nieśmiejący rąk podnieść ani głowy skrzywić,
Aby się etykiecie niczym nie sprzeciwić.
«Czyż nie piękniejsza nasza poczciwa brzezina,
Która jako wieśniaczka, kiedy płacze syna,
Lub wdowa męża, ręce załamie, roztoczy
Po ramionach do ziemi strumienie warkoczy!
Niema z żalu, postawą jak wymownie szlocha!
Czemuż pan Hrabia, jeśli w malarstwie się kocha,
Nie maluje drzew naszych, pośród których siedzi?
Prawdziwie, będą z pana żartować sąsiedzi,
Że mieszkając na żyznej litewskiej równinie,
Malujesz tylko jakieś skały i pustynie». 
«Przyjacielu — rzekł Hrabia — piękne przyrodzenie
Jest formą, tłem, materią; a duszą — natchnienie,
Które na wyobraźni unosi się skrzydłach,
Poleruje się gustem, wspiera na prawidłach.
Nie dość jest przyrodzenia, nie dosyć zapału:
Sztukmistrz musi ulecieć w sfery ideału!
Nie wszystko, co jest piękne, wymalować da się!
Dowiesz się o tym wszystkim z książek w swoim czasie.
Co się tyczy malarstwa: do obrazu trzeba
Punktów widzenia, grupy, ansamblu i nieba,
Nieba włoskiego! Stąd też w kunszcie pejzażów,
Włochy były, są, będą, ojczyzną malarzów!
Stąd też, oprócz Brejgela (lecz nie van der Helle,
Ale pejzażysty: bo są dwaj Brejgele)
I oprócz Ruisdala, na całej północy
Gdzież był pejzażysta który pierwszej mocy?
Niebios, niebios potrzeba». — «Nasz malarz Orłowski,
Przerwała Telimena — miał gust soplicowski.
(Trzeba wiedzieć, że to jest Sopliców choroba,
Że im oprócz ojczyzny nic się nie podoba).
Orłowski, który życie strawił w Peterburku,
Sławny malarz (mam jego kilka szkiców w biurku)
Mieszkał tuż przy cesarzu, na dworze, jak w raju:
A nie uwierzy Hrabia, jak tęsknił po kraju!
Lubił ciągle wspominać swej młodości czasy,
Wystawiał wszystko w Polszcze: ziemię, niebo, lasy…» 
«I miał rozum! — zawołał Tadeusz z zapałem. —
To państwa niebo włoskie, jak o nim słyszałem,
Błękitne, czyste: wszak to jak zamarzła woda;
Czyż nie piękniejsze stokroć wiatr i niepogoda?
U nas dość głowę podnieść: ileż to widoków!
Ileż scen i obrazów z samej gry obłoków!
Bo każda chmura inna: na przykład jesienna
Pełznie jak żółw leniwa, ulewą brzemienna,
I z nieba aż do ziemi spuszcza długie smugi,
Jak rozwite warkocze, to są deszczu strugi;
Chmura z gradem, jak balon szybko z wiatrem leci,
Krągła, ciemnobłękitna, w środku żółto świeci,
Szum wielki słychać wkoło; nawet te codzienne,
Patrzcie państwo, te białe chmurki, jak odmienne!
Zrazu jak stada dzikich gęsi lub łabędzi,
A z tyłu wiatr jak sokół do kupy je pędzi:
Ściskają się, grubieją, rosną — nowe dziwy!
Dostają krzywych karków, rozpuszczają grzywy,
Wysuwają nóg rzędy i po niebios sklepie
Przelatują jak tabun rumaków po stepie:
Wszystkie białe jak srebro, zmieszały się… nagle
Z ich karków rosną maszty, z grzyw szerokie żagle,
Tabun zmienia się w okręt i wspaniale płynie
Cicho, z wolna po niebios błękitnej równinie!»
Hrabia i Telimena poglądali w górę;
Tadeusz jedną ręką pokazał im chmurę,
A drugą ścisnął z lekka rączkę Telimeny.
Kilka już upłynęło minut cichej sceny;
Hrabia rozłożył papier na swym kapeluszu
I wydobył ołówek. Wtem przykry dla uszu
Odezwał się dzwon dworski i zaraz śród lasu
Cichego pełno było krzyku i hałasu.
Hrabia, kiwnąwszy głową, rzekł poważnym tonem:
«Tak to na świecie wszystko los zwykł kończyć dzwonem!…
Rachunki myśli wielkiej, plany wyobraźni,
Zabawki niewinności, uciechy przyjaźni,
Wylania się serc czułych: gdy spiż z dala ryknie,
Wszystko miesza się, zrywa, mąci się i niknie!» 
Tu, obróciwszy czuły wzrok ku Telimenie,
«Cóż zostaje?» A ona mu rzekła: «Wspomnienie!»
I chcąc Hrabiego nieco ułagodzić smutek,
Podała mu urwany kwiatek niezabudek. 
Hrabia go ucałował i na pierś przyszpilał;
Tadeusz z drugiej strony krzak ziela rozchylał,
Widząc, że się ku niemu tym zielem przewija
Coś białego: była to rączka jak lilija;
Pochwycił ją, całował i usty po cichu
Utonął w niej jak pszczoła w liliji kielichu.
Uczuł na ustach zimno; znalazł klucz i biały
Papier w trąbkę zwiniony; był to listek mały.
Porwał, schował w kieszenie; nie wie, co klucz znaczy,
Lecz mu to owa biała kartka wytłumaczy.
Dzwon wciąż dzwonił i echem z głębi cichych lasów
Odezwało się tysiąc krzyków i hałasów.
Odgłos to był szukania i nawoływania,
Hasło zakończonego na dziś grzybobrania;
Odgłos nie smutny wcale ani pogrzebowy,
Jak się Hrabiemu zdało: owszem, obiadowy.
Dzwon ten, w każde południe krzyczący z poddasza,
Gości i czeladź domu na obiad zaprasza:
Tak było w dawnych licznych dworach we zwyczaju
I zostało się w domu Sędziego. Więc z gaju
Wychodziła gromada, niosąca krobeczki,
Koszyki uwiązane końcami chusteczki,
Pełne grzybów; a panny w jednym ręku niosły,
Jako wachlarz zwiniony, borowik rozrosły,
W drugim związane razem jakby polne kwiatki,
Opieńki i rozlicznej barwy surojadki.
Wojski miał muchomora. Z próżnymi przychodzi
Rękami Telimena; z nią panicze młodzi.
Goście weszli w porządku i stanęli kołem.
Podkomorzy najwyższe brał miejsce za stołem:
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się starcom, damom i młodzieży;
Obok stał kwestarz; Sędzia tuż przy bernardynie.
Bernardyn zmówił krótki pacierz po łacinie;
Podano w kolej wódkę: za czym wszyscy siedli,
I chołodziec litewski milczkiem żwawo jedli.
Obiadowano ciszej, niż się zwykle zdarza;
Nikt nie gadał, pomimo wezwań gospodarza.
Strony biorące udział w wielkiej o psów zwadzie,
Myśliły o jutrzejszej walce i zakładzie;
Myśl wielka zwykle usta do milczenia zmusza. 
Telimena, mówiąca wciąż do Tadeusza,
Musiała ku Hrabiemu nieraz się odwrócić,
Nawet na Asesora nieraz okiem rzucić:
Tak ptasznik patrzy w sidło, kędy szczygły zwabia,
I razem w pastkę wróblą. Tadeusz i Hrabia,
Obadwa radzi z siebie, obadwa szczęśliwi,
Obaj pełni nadziei, więc niegadatliwi.
Hrabia na kwiatek dumne opuszczał wejrzenie,
A Tadeusz ukradkiem spozierał w kieszenie,
Czy ów kluczyk nie uciekł? Ręką nawet chwytał
I kręcił kartkę, której dotąd nie przeczytał. 
Sędzia Podkomorzemu węgrzyna, szampana
Dolewał, służył pilnie, ściskał za kolana,
Ale do rozmawiania z nim nie miał ochoty
I widać, że czuł jakieś tajemne kłopoty. 
Przemijały w milczeniu talerze i dania;
Przerwał nareszcie nudny tok obiadowania
Gość niespodziany, szybko wpadając, gajowy;
Nie zważał nawet, że czas właśnie obiadowy,
Pobiegł do pana; widać z postawy i z miny,
Że ważnej i niezwykłej jest posłem nowiny.
Ku niemu oczy całe zwróciło zebranie.
On, odetchnąwszy nieco, rzekł: «Niedźwiedź, mospanie!»
Resztę wszyscy odgadli: że źwierz z matecznika 
Wyszedł, że w zaniemeńską puszczę się przemyka,
Że go trzeba wnet ścigać, wszyscy wraz uznali,
Choć ani się radzili, ani namyślali;
Spólną myśl widać było z uciętych wyrazów,
Z gestów żywych, z wydanych rozlicznych rozkazów,
Które, wychodząc tłumnie, razem z ust tak wielu,
Dążyły przecież wszystkie do jednego celu.
«Na wieś! — zawołał Sędzia — hej! konno, setnika!
Jutro na brzask obława, lecz na ochotnika;
Kto wystąpi z oszczepem, temu z robocizny
Wytrącić dwa szarwarki i pięć dni pańszczyzny». 
«W skok — krzyknął Podkomorzy — okulbaczyć siwą,
Dobiec w cwał do mojego dworu; wziąć co żywo
Dwie pjawki, które w całej okolicy słyną,
Pies zowie się Sprawnikiem, a suka Strapczyną;
Zakneblować im pyski, zawiązać je w miechu,
I przystawić je tutaj konno dla pośpiechu».
«Wańka! — krzyknął na chłopca Asesor po rusku —
Tasak mój sanguszkowski pociągnąć na brusku:
Wiesz, tasak co od księcia miałem w podarunku;
Pas opatrzyć, czy kula jest w każdym ładunku».
«Strzelby — krzyknęli wszyscy — mieć na pogotowiu!»
Asesor wołał ciągle: «Ołowiu, ołowiu!
Formę do kul mam w torbie». — «Do księdza plebana
Dać znać — dodał pan Sędzia — żeby jutro z rana
Mszę miał w kaplicy leśnej: króciuchna oferta 
Za myśliwych, msza zwykła świętego Huberta».
Po wydanych rozkazach nastało milczenie;
Każdy dumał i rzucał dokoła wejrzenie,
Jak gdyby kogoś szukał; z wolna wszystkich oczy
Sędziwa twarz Wojskiego ciągnie i jednoczy:
Znak to był, że szukają na przyszłą wyprawę
Wodza i że Wojskiemu oddają buławę.
Wojski powstał, zrozumiał towarzyszów wolę,
I uderzywszy ręką poważnie po stole,
Pociągnął złocistego z zanadrza łańcuszka,
Na którym wisiał gruby zegarek jak gruszka:
«Jutro — rzekł — pół do piątej, przy leśnej kaplicy
Stawią się bracia strzelcy, wiara obławnicy». 
Rzekł i ruszył od stołu, za nim szedł gajowy;
Oni obmyślić mają i urządzić łowy. 
Tak wodze, gdy na jutro bitwę zapowiedzą,
Żołnierze po obozie broń czyszczą i jedzą,
Lub na płaszczach i siodłach śpią próżni kłopotu,
A wodze śród cichego dumają namiotu. 
Przerwał się obiad, dzień zszedł na kowaniu koni,
Karmieniu psów, zbieraniu i czyszczeniu broni;
U wieczerzy, zaledwo kto przysiadł do stoła;
Nawet strona Kusego z partyją Sokoła,
Przestała dawnym wielkim zatrudniać się sporem:
Pobrawszy się pod ręce, Rejent z Asesorem
Wyszukują ołowiu. Reszta spracowana
Szła spać wcześnie, ażeby przebudzić się z rana.
Księga czwarta
Dyplomatyka i łowy
Zjawisko w papilotach budzi Tadeusza — Za późne postrzeżenie omyłki — Karczma — Emisariusz — Zręczne użycie tabakiery zwraca dyskusję na właściwą drogę — Matecznik — Niedźwiedź — Niebezpieczeństwo Tadeusza i Hrabiego — Trzy strzały — Spór Sagalasówki z Sanguszkówką rozstrzygniony na stronę jednorurki horeszkowskiej — Bigos — Wojskiego powieść o pojedynku Doweyki z Domeyką przerwana szczuciem kota — Koniec powieści o Doweyce i Domeyce.

Rówienniki litewskich wielkich kniaziów, drzewa
Białowieży, Świtezi, Ponar, Kuszelewa!
Których cień spadał niegdyś na koronne głowy
Groźnego Witenesa, wielkiego Mindowy,
I Giedymina, kiedy na Ponarskiej Górze,
Przy ognisku myśliwskim, na niedźwiedziej skórze
Leżał, słuchając pieśni mądrego Lizdejki,
A Wilii widokiem i szumem Wilejki
Ukołysany, marzył o wilku żelaznym,
i zbudzony, za bogów rozkazem wyraźnym
Zbudował miasto Wilno, które w lasach siedzi
Jak wilk pośrodku żubrów, dzików i niedźwiedzi.
Z tego to miasta Wilna, jak z rzymskiej wilczycy,
Wyszedł Kiejstut i Olgierd, i Olgierdowicy,
Równie myśliwi wielcy jak sławni rycerze,
Czyli wroga ścigali, czyli dzikie źwierzę.
Sen myśliwski nam odkrył tajnie przyszłych czasów:
Że Litwie trzeba zawsze żelaza i lasów. 
Knieje! do was ostatni przyjeżdżał na łowy
Ostatni król, co nosił kołpak Witoldowy,
Ostatni z Jagiellonów wojownik szczęśliwy,
I ostatni na Litwie monarcha myśliwy.
Drzewa moje ojczyste! jeśli Niebo zdarzy,
Bym wrócił was oglądać, przyjaciele starzy,
Czyli was znajdę jeszcze? czy dotąd żyjecie?
Wy, koło których niegdyś pełzałem jak dziecię;
Czy żyje wielki Baublis, w którego ogromie
Wiekami wydrążonym, jakby w dobrym domie,
Dwunastu ludzi mogło wieczerzać za stołem?
Czy kwitnie gaj Mendoga pod farnym kościołem?
I tam na Ukrainie czy się dotąd wznosi
Przed Hołowińskch domem, nad brzegami Rosi,
Lipa tak rozrośniona, że pod jej cieniami
Sto młodzieńców, sto panien szło w taniec parami?
Pomniki nasze! ileż co rok was pożera
Kupiecka lub rządowa, moskiewska siekiera!
Nie zostawia przytułku ni leśnym śpiewakom,
Ni wieszczom, którym cień wasz tak miły jak ptakom.
Wszak lipa czarnoleska, na głos Jana czuła,
Tyle rymów natchnęła! Wszak ów dąb gaduła
Kozackiemu wieszczowi tyle cudów śpiewa! 
Ja ileż wam winienem, o domowe drzewa!
Błahy strzelec, uchodząc szyderstw towarzyszy
Za chybioną źwierzynę, ileż w waszej ciszy
Upolowałem dumań, gdy w dzikim ostępie,
Zapomniawszy o łowach, usiadłem na kępie,
A koło mnie srebrzył się tu mech siwobrody,
Zlany granatem czarnej, zgniecionej jagody,
A tam się czerwieniły wrzosiste pagórki,
Strojne w brusznice jakby w koralów paciórki.
Wokoło była ciemność; gałęzie u góry
Wisiały jak zielone, gęste, niskie chmury;
Wicher kędyś nad sklepem szalał nieruchomym,
Jękiem, szumami, wyciem, łoskotami, gromem:
Dziwny, odurzający hałas! Mnie się zdało,
Że tam nad głową morze wiszące szalało. 
Na dole jak ruiny miast: tu wywrót dębu
Wysterka z ziemi na kształt ogromnego zrębu;
Na nim oparte, jak ścian i kolumn obłamy,
Tam gałęziste kłody, tu wpół zgniłe tramy 
Ogrodzone parkanem traw. W środek tarasu
Zajrzeć straszno, tam siedzą gospodarze lasu,
Dziki, niedźwiedzie, wilki; u wrót leżą kości
Na pół zgryzione jakichś nieostrożnych gości.
Czasem wymkną się w górę przez trawy zielenie,
Jakby dwa wodotryski, dwa rogi jelenie,
I mignie między drzewa źwierz żółtawym pasem,
Jak promień, kiedy wpadłszy gaśnie między lasem. 
I znowu cichość w dole. Dzięcioł na jedlinie 
Stuka z lekka i dalej odlatuje, ginie,
Schował się, ale dziobem nie przestaje pukać,
Jak dziecko, gdy schowane woła, by go szukać. 
Bliżej siedzi wiewiórka, orzech w łapkach trzyma,
Gryzie go; zawiesiła kitkę nad oczyma,
Jak pióro nad szyszakiem u kirasyjera:
Chociaż tak osłoniona, dokoła spoziera,
Dostrzegłszy gościa, skacze gajów tanecznica
Z drzew na drzewa, miga się jako błyskawica;
Na koniec w niewidzialny otwór pnia przepada,
Jak wracająca w drzewo rodzime dryjada. 
Znowu cicho. 
Wtem, gałąź wstrząsła się trącona,
I pomiędzy jarzębin rozsunione grona
Kraśniejsze od jarzębin zajaśniały lica:
To jagód lub orzechów zbieraczka, dziewica.
W krobeczce z prostej kory podaje zebrane
Bruśnice świeże jako jej usta rumiane.
Obok młodzieniec idzie, leszczynę nagina:
Chwyta w lot migające orzechy dziewczyna.
Wtem, usłyszeli odgłos rogów i psów granie:
Zgadują, że się ku nim zbliża polowanie,
I pomiędzy gałęzi gęstwę, pełni trwogi,
Zniknęli nagle z oczu jako leśne bogi. 
W Soplicowie ruch wielki. Lecz ni psów hałasy,
Ani rżące rumaki, skrzypiące kolasy,
Ni odgłos trąb dających hasło polowania
Nie mogły Tadeusza wyciągnąć z posłania;
Ubrany padłszy w łóżko, spał jak bobak w norze.
Nikt z młodzieży nie myślał szukać go po dworze;
Każdy sobą zajęty śpieszył, gdzie kazano;
O towarzyszu sennym całkiem zapomniano. 
On chrapał. Słońce w otwór, co śród okienicy
Wyrżnięty był w kształt serca, wpadło do ciemnicy
Słupem ognistym, prosto sennemu na czoło.
On jeszcze chciał zadrzemać i kręcił się wkoło,
Chroniąc się blasku. Nagle usłyszał stuknienie,
Przebudził się: wesołe było przebudzenie.
Czuł się rzeźwym jak ptaszek, z lekkością oddychał,
Czuł się szczęśliwym, sam się do siebie uśmiechał:
Myśląc o wszystkim, co mu wczora się zdarzyło,
Rumienił się i wzdychał, i serce mu biło.
Spojrzał w okno, o dziwy! W promieni przezroczu,
W owym sercu, błyszczało dwoje jasnych oczu,
Szeroko otworzonych, jak zwykle wejrzenie,
Kiedy z jasności dziennej przedziera się w cienie.
Ujrzał i małą rączkę, niby wachlarz z boku
Nadstawioną ku słońcu dla ochrony wzroku;
Palce drobne, zwrócone na światło różowe,
Czerwieniły się na wskroś jakby rubinowe. 
Usta widział ciekawe, roztulone nieco,
I ząbki, co jak perły śród koralów świecą,
I lica, choć od słońca zasłaniane dłonią
Różową, same całe jak róże się płonią.
Tadeusz spał pod oknem; sam ukryty w cieniu,
Leżąc na wznak, cudnemu dziwił się zjawieniu
I miał je tuż nad sobą, ledwie nie na twarzy:
Nie wiedział, czy to jawa, czyli mu się marzy
Jedna z tych miłych, jasnych twarzyczek dziecinnych,
Które pomnim widziane we śnie lat niewinnych. 
Twarzyczka schyliła się — ujrzał, drżąc z bojaźni
I radości, niestety! ujrzał najwyraźniej,
Przypomniał, poznał włos ów krótki, jasnozłoty,
W drobne, jako śnieg białe, zwity papiloty,
Niby srebrzyste strączki, co od słońca blasku
Świeciły jak korona na świętych obrazku.
Zerwał się i widzenie zaraz uleciało
Przestraszone łoskotem; czekał, nie wracało!
Tylko usłyszał znowu trzykrotne stukanie
I słowa: «Niech pan wstaje, czas na polowanie.
Pan zaspał». Skoczył z łóżka i obu rękami
Pchnął okienicę, że aż trzasła zawiasami
I rozwarłszy się w obie uderzyła ściany;
Wyskoczył, patrzył wkoło zdumiony, zmieszany,
Nic nie widział, nie dostrzegł niczyjego śladu.
Niedaleko od okna był parkan od sadu,
Na nim chmielowe liście i kwieciste wieńce
Chwiały się; czy je lekkie potrąciły ręce?
Czy wiatr ruszył? Tadeusz długo patrzył na nie,
Nie śmiał iść w ogród; tylko wsparł się na parkanie,
Oczy podniósł i z palcem do ust przyciśnionym
Kazał sam sobie milczeć, by słowem kwapionem
Nie rozerwał milczenia; potem w czoło stukał,
Niby do wspomnień dawnych uśpionych w nim pukał,
Na koniec, gryząc palce, do krwi się zadrasnął
I na cały głos: «Dobrze, dobrze mi tak!» wrzasnął.
We dworze, gdzie przed chwilą tyle było krzyku,
Teraz pusto i głucho jak na mogilniku:
Wszyscy ruszyli w pole. Tadeusz nadstawił
Uszu i ręce do nich jak trąbki przyprawił;
Słuchał, aż mu wiatr przyniósł, wiejący od puszczy,
Odgłosy trąb i wrzaski polującej tłuszczy. 
Koń Tadeusza czekał w stajni osiodłany.
Wziął więc flintę, skoczył nań i jak opętany
Pędził ku karczmom, które stały przy kaplicy,
Kędy mieli się rankiem zebrać obławnicy. 
Dwie chyliły się karczmy po dwóch stronach drogi,
Oknami wzajem sobie grożące jak wrogi.
Stara należy z prawa do zamku dziedzica;
Nową, na złość zamkowi, postawił Soplica.
W tamtej, jak w swym dziedzictwie, rej wodził Gerwazy,
W tej najwyższe za stołem brał miejsce Protazy. 
Nowa karczma nie była ciekawa z pozoru.
Stara wedle dawnego zbudowana wzoru,
Który był wymyślony od tyryjskich cieśli,
A potem go Żydowie po świecie roznieśli:
Rodzaj architektury obcym budowniczym
Wcale nieznany; my go od Żydów dziedziczym. 
Karczma z przodu jak korab, z tyłu jak świątynia:
Korab, istna Noego czworogranna skrzynia,
Znany dziś pod prostackim nazwiskiem stodoły;
Tam różne są zwierzęta, konie, krowy, woły,
Kozy brodate; w górze zaś ptactwa gromady,
I płazów choć po parze, są też i owady. 
Część tylna, na kształt dziwnej świątyni stawiona,
Przypomina z pozoru ów gmach Salomona,
Który pierwsi ćwiczeni w budowań rzemieśle
Hiramscy na Syjonie wystawili cieśle.
Żydzi go naśladują dotąd we swych szkołach,
A szkół rysunek widny w karczmach i stodołach.
Dach z dranic i ze słomy, spiczasty, zadarty,
Pogięty jako kołpak żydowski podarty.
Ze szczytu wytryskują krużganku krawędzie,
Oparte na drewnianym licznych kolumn rzędzie.
Kolumny, co jest wielkie architektów dziwo,
Trwałe, chociaż wpół zgniłe i stawione krzywo,
Jako w wieży pizańskiej, nie podług modelów
Greckich, bo są bez podstaw i bez kapitelów.
Nad kolumnami biegą wpółokrągłe łuki,
Także z drzewa, gotyckiej naśladowstwo sztuki.
Z wierzchu ozdoby sztuczne, nie rylcem, nie dłutem,
Ale zręcznie ciesielskim wyrzezane sklutem,
Krzywe jak szabasowych ramiona świeczników;
Na końcu wiszą gałki, coś na kształt guzików,
Które Żydzi modląc się na łbach zawieszają
I które po swojemu cyces nazywają.
Słowem, z daleka karczma chwiejąca się, krzywa,
Podobna jest do Żyda, gdy się modląc kiwa:
Dach jak czapka, jak broda strzecha roztrzęsiona,
Ściany dymne i brudne jak czarna opona,
A z przodu rzeźba sterczy jak cyces na czole. 
W środku karczmy jest podział jak w żydowskiej szkole:
Jedna część, pełna izbic ciasnych i podłużnych,
Służy dla dam wyłącznie i panów podróżnych;
W drugiej ogromna sala: koło każdej ściany
Ciągnie się wielonożny stół wąski, drewniany;
Przy nim stołki, choć niższe, podobne do stoła,
Jako dzieci do ojca.
Na stołkach dokoła
Siedziały chłopy, chłopki tudzież szlachta drobna,
Wszyscy rzędem; ekonom sam siedział z osobna.
Po rannej mszy z kaplicy, że była niedziela,
Zabawić się i wypić przyszli do Jankiela.
Przy każdym już szumiała siwą wódką czarka,
Ponad wszystkimi z butlą biegała szynkarka. 
W środku arendarz Jankiel, w długim aż do ziemi
Szarafanie, zapiętym haftkami srebrnemi,
Rękę jedną za czarny pas jedwabny wsadził,
Drugą poważnie sobie siwą brodę gładził;
Rzucając wkoło okiem rozkazy wydawał,
Witał wchodzących gości, przy siedzących stawał
Zagajając rozmowę, kłótliwych zagadzał,
Lecz nie służył nikomu: tylko się przechadzał. 
Żyd stary i powszechnie znany z poczciwości,
Od lat wielu dzierżawił karczmę, a nikt z włości,
Nikt ze szlachty nie zaniósł nań skargi do dworu.
O cóż skarżyć? Miał trunki dobre do wyboru,
Rachował się ostrożnie, lecz bez oszukaństwa,
Ochoty nie zabraniał, nie cierpiał pijaństwa,
Zabaw wielki miłośnik: u niego wesele
I chrzciny obchodzono, on w każdą niedzielę
Kazał do siebie ze wsi przychodzić muzyce,
Przy której i basetla była, i kozice. 
Muzykę znał, sam słynął muzycznym talentem;
Z cymbałami, narodu swego instrumentem,
Chadzał niegdyś po dworach i graniem zdumiewał,
I pieśniami, bo biegle i uczenie śpiewał.
Chociaż Żyd, dosyć czystą miał polską wymowę,
Szczególniej zaś polubił pieśni narodowe;
Przywoził mnóstwo z każdej za Niemen wyprawy,
Kołomyjek z Halicza, mazurów z Warszawy;
Wieść, nie wiem czyli pewna, w całej okolicy
Głosiła, że on pierwszy przywiózł z zagranicy
I upowszechnił wówczas, w tamecznym powiecie,
Ową piosenkę, sławną dziś na całym świecie,
A którą po raz pierwszy na ziemi Auzonów 
Wygrały Włochom polskie trąby legijonów.
Talent śpiewania bardzo na Litwie popłaca,
Jedna miłość u ludzi, wsławia i wzbogaca:
Jankiel zrobił majątek; syt zysków i chwały,
Zawiesił dźwięcznostrunne na ścianie cymbały;
Osiadłszy z dziećmi w karczmie, zatrudniał się szynkiem,
Przy tym w pobliskim mieście był też podrabinkiem,
A zawsze miłym wszędzie gościem i domowym
Doradcą; znał się dobrze na handlu zbożowym,
Na wicinnym: potrzebna jest znajomość taka
Na wsi. Miał także sławę dobrego Polaka. 
On pierwszy zgodził kłótnie, często nawet krwawe,
Między dwiema karczmami: obie wziął w dzierżawę;
Szanowali go równie i starzy stronnicy
Horeszkowscy, i słudzy Sędziego Soplicy.
On sam powagę umiał utrzymać nad groźnym
Klucznikiem horeszkowskim i kłótliwym Woźnym;
Przed Jankielem tłumili dawne swe urazy
Gerwazy, groźny ręką, językiem Protazy.
Gerwazego nie było; ruszył na obławę,
Nie chcąc, aby tak ważną i trudną wyprawę
Odbył sam Hrabia, młody i niedoświadczony;
Poszedł więc z nim dla rady tudzież dla obrony. 
Dziś miejsce Gerwazego, najdalsze od progu,
Między dwiema ławami, w samym karczmy rogu,
Zwane pokuciem, kwestarz ksiądz Robak zajmował.
Jankiel go tam posadził. Widać, że szanował
Wysoko bernardyna: bo skoro dostrzegał
Ubytek w jego szklance, natychmiast podbiegał
I rozkazał dolewać lipcowego miodu.
Słychać, że z bernardynem znali się za młodu,
Kędyś tam w cudzych krajach. Robak często chadzał
Nocą do karczmy, tajnie z Żydem się naradzał
O ważnych rzeczach; słychać było, że towary
Ksiądz przemycał — lecz potwarz ta niegodna wiary. 
Robak, wsparty na stole, wpół głośno rozprawiał,
Tłum szlachty go otaczał i uszy nadstawiał,
I nosy ku księdzowskiej chylił tabakierze;
Brano z niej, i kichała szlachta jak moździerze. 
«Reverendissime — rzekł kichnąwszy Skołuba —
To mi tabaka, co to idzie aż do czuba!
Od czasu jak nos dźwigam (tu głasnął nos długi)
Takiej nie zażywałem (tu kichnął raz drugi);
Prawdziwa bernardynka, pewnie z Kowna rodem,
Miasta sławnego w świecie tabaką i miodem.
Byłem tam lat już…» — Robak przerwał mu: «Na zdrowie
Wszystkim waszmościom, moi mościwi panowie!
Co się tabaki tyczy, hem, ona pochodzi
Z dalszej strony, niż myśli Skołuba dobrodziéj:
Pochodzi z Jasnej Góry. Księża paulinowie
Tabakę taką robią w mieście Częstochowie,
Kędy jest obraz tylu cudami wsławiony,
Bogarodzicy Panny, Królowej Korony
Polskiej… zowią ją dotąd i Księżną Litewską —
Koronęć jeszcze dotąd piastuje królewską…
Lecz na Litewskim Księstwie teraz syzma siedzi!»
«Z Częstochowy? — rzekł Wilbik. — Byłem tam w spowiedzi,
Kiedym na odpust chodził lat temu trzydzieście.
Czy to prawda, że Francuz gości teraz w mieście,
Że chce kościół rozwalać i skarbiec zabierze:
Bo to wszystko w Litewskim stoi Kuryjerze?»
«Nieprawda — rzekł bernardyn — nie! Pan Najjaśniejszy,
Napoleon, katolik jest najprzykładniejszy:
Wszak go papież namaścił, żyją z sobą w zgodzie
I nawracają ludzi w francuskim narodzie,
Który się trochę popsuł. Prawda, z Częstochowy
Oddano wiele srebra na skarb narodowy
Dla ojczyzny, dla Polski; sam Pan Bóg tak każe:
Skarbcem ojczyzny zawsze są Jego ołtarze.
Wszakże w Warszawskim Księstwie mamy sto tysięcy
Wojska polskiego, może wkrótce będzie więcéj:
A któż wojsko opłaci? czy nie wy, Litwini?
Wy tylko grosz dajecie do moskiewskiej skrzyni».
«Kat by dał — krzyknął Wilbik — gwałtem od nas biorą». 
«Oj, dobrodzieju — chłopek ozwał się z pokorą,
Pokłoniwszy się księdzu i skrobiąc się w głowę —
Już to szlachcie, to jeszcze bieda przez połowę;
Lecz nas drą jak na łyka…» «Cham! — Skołuba krzyknął —
Głupi, tobieć to lepiej, tyś chłopie przywyknął,
Jak węgorz do odarcia: lecz nam urodzonym,
Nam wielmożnym, do złotych swobód wzwyczajonym!
Ach, bracia! wszak to dawniej szlachcic na zagrodzie…
(«Tak, tak — krzyknęli wszyscy — równy wojewodzie!») 
Dziś nam szlachectwa przeczą, każą nam drabować 
Papiery, i szlachectwa papierem próbować».
«Jeszcze Waszeci mniejsza — zawołał Juraha —
Waszeć z pradziadów chłopów uszlachcony szlacha;
Ale ja, z kniaziów! Pytać u mnie o patenta,
Kiedym został szlachcicem? Sam Bóg to pamięta!
Niechaj Moskal w las idzie pytać się dębiny,
Kto jej dał patent rosnąć nad wszystkie krzewiny».
«Kniaziu — rzekł Żagiel — świeć waść baki lada komu,
Tu znajdziesz pono mitry i w niejednym domu».
«Waść ma krzyż w herbie — wołał Podhajski — to skryta
Aluzyja, że w rodzie bywał neofita».
«Fałsz — przerwał Birbasz — Przecież ja z tatarskich hrabiów
Pochodzę, a mam krzyże nad herbem Korabiów».
«Poraj — krzyknął Mickiewicz — z mitrą w polu złotym,
Herb książęcy, Stryjkowski gęsto pisze o tym». 
Za czym wielkie powstały w całej karczmie szmery.
Ksiądz bernardyn uciekł się do swej tabakiery;
W kolej częstował mówców. Gwar zaraz ucichnął;
Każdy zażył przez grzeczność i kilkakroć kichnął. 
Bernardyn, korzystając z przerwy, mówił daléj:
«Oj, wielcy ludzie od tej tabaki kichali!
Czy uwierzycie państwo, że z tej tabakiery,
Pan jenerał Dąbrowski zażył razy cztery?»
«Dąbrowski?» — zawołali. «Tak, tak, on, jenerał.
Byłem w obozie, gdy on Gdańsk Niemcom odbierał;
Miał coś pisać; bojąc się, ażeby nie zasnął,
Zażył, kichnął, dwakroć mię po ramieniu klasnął:
»Księże Robaku — mówił — księże bernardynie,
Obaczymy się w Litwie może nim rok minie;
Powiedz Litwinom, niech mnie czekają z tabaką
Częstochowską, nie biorę innej tylko taką».
Mowa księdza wzbudziła takie zadziwienie,
Taką radość, że całe huczne zgromadzenie
Milczało chwilę; potem na pół ciche słowa
Powtarzano: «Tabaka z Polski? Częstochowa?
Dąbrowski? Z ziemi włoskiej?…» Aż na koniec razem,
Jakby myśl z myślą, wyraz sam zbiegł się z wyrazem,
Wszyscy jednogłośnie, jak na dane hasło,
Krzyknęli: «Dąbrowskiego!» Wszystko razem wrzasło,
Wszystko się uścisnęło: chłop z tatarskim hrabią,
Mitra z Krzyżem, Poraje z Gryfem i z Korabią;
Zapomnieli wszystkiego, nawet bernardyna,
Tylko śpiewali krzycząc: «Wódki, miodu, wina!» 
Długo się przysłuchiwał ksiądz Robak piosence,
Na koniec chciał ją przerwać; wziął w obydwie ręce
Tabakierkę, kichaniem melodyję zmieszał,
I nim się nastroili, tak mówić pośpieszał:
«Chwalicie mą tabakę, mości dobrodzieje;
Obaczcież, co się wewnątrz tabakierki dzieje».
Tu, wycierając chustką zabrudzone denko,
Pokazał malowaną armiję maleńką
Jak rój much; w środku jeden człowiek na rumaku,
Wielki jako chrząszcz, siedział, pewnie wódz orszaku;
Spinał konia, jak gdyby chciał skakać w niebiosa,
Jedną rękę na cuglach, drugą miał u nosa:
«Przypatrzcie się — rzekł Robak — tej groźnej postawie:
Zgadnijcie czyja? — Wszyscy patrzyli ciekawie.—
Wielki to człowiek, cesarz, ale nie Moskali,
Ich carowie tabaki nigdy nie bierali…»
«Wielki człowiek — zawołał Cydzik — a w kapocie?
Ja myśliłem, że wielcy ludzie chodzą w złocie:
Bo u Moskalów lada jenerał, mospanie,
To tak świeci się w złocie jak szczupak w szafranie».
«Ba — przerwał Rymsza — przecież widziałem za młodu
Kościuszkę, naczelnika naszego narodu:
Wielki człowiek! A chodził w krakowskiej sukmanie,
To jest czamarce». «W jakiej czamarce, mospanie? —
Odparł Wilbik. — To przecież zwano taratatką».
«Ale tamta z frędzlami, ta jest całkiem gładką» —
Krzyknął Mickiewicz. Zatem wszczynały się swary
O różnych taratatki kształtach i czamary.
Przemyślny Robak, widząc, że się tak rozpryska
Rozmowa, jął ją znowu zbierać do ogniska,
Do swojej tabakiery; częstował, kichali,
Życzyli sobie zdrowia, on rzecz ciągnął daléj:
«Gdy cesarz Napoleon w potyczce zażywa
Raz po raz, to znak pewny, że bitwę wygrywa.
Na przykład pod Austerlitz: Francuzi tak stali
Z armatami, a na nich biegła ćma Moskali.
Cesarz patrzył i milczał. Co Francuzi strzelą,
To Moskale pułkami jak trawa się ścielą:
Pułk za pułkiem cwałował i spadał z kulbaki;
Co pułk spadnie, to cesarz zażyje tabaki.
Aż w końcu, Aleksander ze swoim braciszkiem
Konstantym i z niemieckim cesarzem Franciszkiem,
W nogi z pola; więc cesarz, widząc, że po walce,
Spojrzał na nich, zaśmiał się i otrząsnął palce.
Otóż, jeśli kto z panów, coście tu przytomni,
Będzie w wojsku cesarza, niech to sobie wspomni».
«Ach — zawołał Skołuba — mój księże kwestarzu!
Kiedyż to będzie! Wszak to ile w kalendarzu
Jest świąt, na każde święto Francuzów nam wróżą:
Wygląda człek, wygląda, aż się oczy mrużą;
A Moskal jak nas trzymał, tak trzyma za szyję.
Pono nim słońce wnidzie, rosa oczy wyje».
«Mospanie — rzekł bernardyn — babska rzecz narzekać,
A żydowska rzecz ręce założywszy czekać,
Nim kto w karczmę zajedzie i do drzwi zapuka.
Z Napoleonem pobić Moskalów nie sztuka.
Jużci on Szwabom skórę trzy razy wymłócił,
Brzydkie Prusactwo zdeptał, Anglików wyrzucił
Het za morze, Moskalom zapewne wygodzi;
Ale co stąd wyniknie, wie asan dobrodziéj?
Oto, szlachta litewska wtenczas na koń wsiędzie 
I szable weźmie, kiedy bić się z kim nie będzie;
Napoleon sam wszystkich pobiwszy, nareszcie
Powie: »Obejdę się ja bez was, kto jesteście?«
Więc nie dość gościa czekać, nie dość i zaprosić,
Trzeba czeladkę zebrać i stoły pownosić,
A przed ucztą potrzeba dom oczyścić z śmieci,
Oczyścić dom, powtarzam, oczyścić dom, dzieci!» 
Nastąpiło milczenie, potem głosy w tłumie:
«Jakże to dom oczyścić, jak to ksiądz rozumie?
Jużci my wszystko zrobim, na wszystko gotowi;
Tylko niech ksiądz dobrodziej jaśniej się wysłowi».
Ksiądz poglądał za okno, przerwawszy rozmowę;
Ujrzał coś ciekawego, z okna wytknął głowę,
Po chwili rzekł powstając: «Dziś czasu nie mamy;
Potem o tym obszerniej z sobą pogadamy.
Jutro będę dla sprawy w powiatowym mieście;
I do waszmościów z drogi zajadę po kweście».
«Niech też do Niehrymowa ksiądz na nocleg zdąży —
Rzekł ekonom — rad będzie księdzu pan chorąży;
Wszakże na Litwie stare powiada przysłowie:
Szczęśliwy człowiek, jako kwestarz w Niehrymowie!»
«I do nas — rzekł Zubkowski — wstąp jeżeli łaska;
Znajdzie się tam półsztuczek płótna, masła faska,
Baran lub krówka; wspomnij księże na te słowa:
Szczęśliwy człowiek, trafił jak ksiądz do Zubkowa».
«I do nas» — rzekł Skołuba. «Do nas — Terajewicz —
Żaden bernardyn głodny nie wyszedł z Pucewicz».
Tak cała szlachta prośbą i obietnicami
Przeprowadzała księdza; on już był za drzwiami. 
On już pierwej przez okno ujrzał Tadeusza,
Który leciał gościńcem, w cwał, bez kapelusza,
Z głową schyloną, bladym, posępnym obliczem,
A konia ustawicznie bódł i kropił biczem.
Ten widok bardzo księdza bernardyna zmieszał,
Więc za młodzieńcem kroki szybkimi pośpieszał
Do wielkiej puszczy, która, jako oko sięga,
Czerniła się na całym brzegu widnokręga.
Któż zbadał puszcz litewskich przepastne krainy,
Aż do samego środka, do jądra gęstwiny?
Rybak ledwie u brzegów nawiedza dno morza;
Myśliwiec krąży koło puszcz litewskich łoża,
Zna je ledwie po wierzchu, ich postać, ich lice:
Lecz obce mu ich wnętrzne serca tajemnice;
Wieść tylko albo bajka wie, co się w nich dzieje.
Bo gdybyś przeszedł bory i podszyte knieje,
Trafisz w głębi na wielki wał pniów, kłód, korzeni,
Obronny trzęsawicą, tysiącem strumieni
I siecią zielsk zarosłych, i kopcami mrowisk,
Gniazdami os, szerszeniów, kłębami wężowisk.
Gdybyś i te zapory zmógł nadludzkim męstwem,
Dalej spotkać się z większym masz niebezpieczeństwem:
Dalej co krok czyhają, niby wilcze doły,
Małe jeziorka, trawą zarosłe na poły,
Tak głębokie, że ludzie dna ich nie dośledzą
(Wielkie jest podobieństwo, że diabły tam siedzą).
Woda tych studni sklni się, plamista rdzą krwawą,
A z wnętrza ciągle dymi, zionąc woń plugawą,
Od której drzewa wkoło tracą liść i korę;
Łyse, skarłowaciałe, robaczliwe, chore,
Pochyliwszy konary mchem kołtunowate
I pnie garbiąc, brzydkimi grzybami brodate,
Siedzą wokoło wody jak czarownic kupa
Grzejąca się nad kotłem, w którym warzą trupa. 
Za tymi jeziorkami już nie tylko krokiem,
Ale daremnie nawet zapuszczać się okiem,
Bo tam już wszystko mglistym zakryte obłokiem,
Co się wiecznie ze trzęskich oparzelisk wznosi.
A za tą mgłą na koniec (jak wieść gminna głosi)
Ciągnie się bardzo piękna, żyzna okolica,
Główna królestwa zwierząt i roślin stolica.
W niej są złożone wszystkich drzew i ziół nasiona,
Z których się rozrastają na świat ich plemiona;
W niej, jak w arce Noego, z wszelkich zwierząt rodu
Jedna przynajmniej para chowa się dla płodu.
W samym środku (jak słychać) mają swoje dwory
Dawny Tur, Żubr i Niedźwiedź, puszcz imperatory;
Około nich na drzewach gnieździ się Ryś bystry
I żarłoczny Rosomak jak czujne ministry;
Dalej zaś, jak podwładni szlachetni wasale,
Mieszkają Dziki, Wilki i Łosie rogale.
Nad głowami Sokoły i Orłowie dzicy,
Żyjący z pańskich stołów dworscy zausznicy.
Te pary zwierząt główne i patryjarchalne,
Ukryte w jądrze puszczy, światu niewidzialne,
Dzieci swe ślą dla osad za granicę lasu,
A sami we stolicy używają wczasu;
Nie giną nigdy bronią sieczną ani palną,
Lecz starzy umierają śmiercią naturalną.
Mają też i swój cmentarz, kędy bliscy śmierci,
Ptaki składają pióra, czworonogi sierci:
Niedźwiedź, gdy zjadłszy zęby, strawy nie przeżuwa,
Jeleń zgrzybiały, gdy już ledwie nogi suwa,
Zając sędziwy, gdy mu już krew w żyłach krzepnie,
Kruk, gdy już posiwieje, sokół, gdy oślepnie,
Orzeł, gdy mu dziób stary tak się w kabłąk skrzywi,
Że zamknięty na wieki już gardła nie żywi,
Idą na cmentarz. Nawet mniejszy zwierz, raniony
Lub chory, bieży umrzeć w swe ojczyste strony.
Stąd to w miejscach dostępnych, kędy człowiek gości,
Nie znajdują się nigdy martwych zwierząt kości.
Słychać, że tam w stolicy między zwierzętami
Dobre są obyczaje, bo rządzą się sami;
Jeszcze cywilizacją ludzką nie popsuci,
Nie znają praw własności, która świat nasz kłóci,
Nie znają pojedynków ni wojennej sztuki.
Jak ojce żyły w raju, tak dziś żyją wnuki,
Dzikie i swojskie razem, w miłości i zgodzie,
Nigdy jeden drugiego nie kąsa ni bodzie.
Nawet gdyby tam człowiek wpadł, chociaż niezbrojny,
Toby środkiem bestyi przechodził spokojny;
One by nań patrzyły tym wzrokiem zdziwienia,
Jakim w owym ostatnim szóstym dniu stworzenia
Ojce ich pierwsze, co się w ogrójcu gnieździły,
Patrzyły na Adama, nim się z nim skłóciły.
Szczęściem, człowiek nie zbłądzi do tego ostępu,
Bo Trud, i Trwoga, i Śmierć bronią mu przystępu. 
Czasem tylko w pogoni zaciekłe ogary,
Wpadłszy niebacznie między bagna, mchy i jary,
Wnętrznej ich okropności rażone widokiem,
Uciekają skowycząc z obłąkanym wzrokiem;
I długo potem ręką pana już głaskane,
Drżą jeszcze u nóg jego strachem opętane.
Te puszcz stołeczne, ludziom nieznane tajniki,
W języku swoim strzelcy zowią: mateczniki. 
Głupi niedźwiedziu! gdybyś w mateczniku siedział,
Nigdy by się o tobie Wojski nie dowiedział;
Ale czyli pasieki zwabiła cię wonność,
Czy uczułeś do owsa dojrzałego skłonność,
Wyszedłeś na brzeg puszczy, gdzie się las przerzedził,
I tam zaraz leśniczy bytność twą wyśledził,
I zaraz obsaczniki, chytre nasłał szpiegi,
By poznać, gdzie popasasz i gdzie masz noclegi.
Teraz Wojski z obławą, już od matecznika
Postawiwszy szeregi, odwrót ci zamyka.
Tadeusz się dowiedział, że niemało czasu
Już przeszło, jak ogary wpadły w otchłań lasu.
Cicho. Próżno myśliwi natężają ucha;
Próżno jak najciekawszej mowy każdy słucha
Milczenia, długo w miejscu nieruchomy czeka:
Tylko muzyka puszczy gra do nich z daleka. 
Psy nurtują po puszczy, jak pod morzem nurki,
A strzelcy, obróciwszy do lasu dwururki,
Patrzą Wojskiego. Ukląkł, ziemię uchem pyta;
Jako w twarzy lekarza wzrok przyjaciół czyta
Wyrok życia lub zgonu miłej im osoby,
Tak strzelcy, ufni w sztuki Wojskiego sposoby,
Topili w nim spojrzenia nadziei i trwogi.
«Jest! jest!» — wyrzekł półgłosem, zerwał się na nogi.
On słyszał! Oni jeszcze słuchali; nareszcie
Słyszą: jeden pies wrzasnął, potem dwa, dwadzieście,
Wszystkie razem ogary rozpierzchnioną zgrają
Doławiają się, wrzeszczą, wpadły na trop, grają,
Ujadają. Już nie jest to powolne granie
Psów goniących zająca, lisa albo łanie;
Lecz wciąż wrzask krótki, częsty, ucinany, zjadły;
To nie na ślad daleki ogary napadły:
Na oko gonią. Nagle ustał krzyk pogoni,
Doszli zwierza. Wrzask znowu, skowyt: zwierz się broni
I zapewne kaleczy; śród ogarów grania 
Słychać coraz to częściej jęk psiego konania. 
Strzelcy stali i każdy ze strzelbą gotową
Wygiął się jak łuk naprzód z wciśnioną w las głową.
Nie mogą dłużej czekać! Już ze stanowiska
Jeden za drugim zmyka i w puszczę się wciska,
Chcą pierwsi spotkać źwierza: choć Wojski ostrzegał,
Choć Wojski stanowiska na koniu obiegał,
Krzycząc, że czy kto prostym chłopem, czy paniczem,
Jeżeli z miejsca zejdzie, dostanie w grzbiet smyczem!
Nie było rady! Wszyscy pomimo zakazu
W las pobiegli. Trzy strzelby huknęły od razu;
Potem wciąż kanonada, aż głośniej nad strzały
Ryknął niedźwiedź i echem napełnił las cały.
Ryk okropny, boleści, wściekłości, rozpaczy;
Za nim wrzask psów, krzyk strzelców, trąby dojeżdżaczy
Grzmiały ze środka puszczy. Strzelcy — ci w las śpieszą,
Tamci kurki odwodzą, a wszyscy się cieszą;
Jeden Wojski w żałości, krzyczy, że chybiono.
Strzelcy i obławnicy poszli jedną stroną
Na przełaj źwierza, między ostępem i puszczą,
A niedźwiedź, odstraszony psów i ludzi tłuszczą,
Zwrócił się nazad w miejsca mniej pilnie strzeżone
Ku polom, skąd już zeszły strzelcy rozstawione,
Gdzie tylko pozostali z mnogich łowczych szyków
Wojski, Tadeusz, Hrabia, z kilką obławników.
Tu las był rzadszy. Słychać z głębi ryk, trzask łomu;
Aż z gęstwy, jak z chmur, wypadł niedźwiedź na kształt gromu;
Wkoło psy gonią, straszą, rwą; on wstał na nogi
Tylne i spojrzał wkoło, rykiem strasząc wrogi,
I przednimi łapami to drzewa korzenie,
To pniaki osmalone, to wrosłe kamienie
Rwał, waląc w psów i w ludzi, aż wyłamał drzewo.
Kręcąc nim jak maczugą na prawo, na lewo,
Runął wprost na ostatnich strażników obławy:
Hrabię i Tadeusza. Oni bez obawy
Stoją w kroku, na źwierza wytknęli flint rury,
Jako dwa konduktory w łono ciemnej chmury;
Aż oba jednym razem pociągnęli kurki
(Niedoświadczeni!), razem zagrzmiały dwururki:
Chybili. Niedźwiedź skoczył; oni tuż utkwiony
Oszczep jeden chwycili czterema ramiony,
Wydzierali go sobie. Spojrzą, aż tu z pyska
Wielkiego, czerwonego dwa rzędy kłów błyska,
I łapa z pazurami już się na łby spuszcza;
Pobledli, w tył skoczyli i, gdzie rzednie puszcza,
Zmykali. Zwierz za nimi wspiął się, już pazury
Zahaczał, chybił, podbiegł, wspiął się znów do góry
I czarną łapą sięgał Hrabiego włos płowy.
Zdarłby mu czaszkę z mozgów jak kapelusz z głowy,
Gdy Asesor z Rejentem wyskoczyli z boków,
A Gerwazy biegł z przodu o jakie sto kroków,
Z nim Robak, choć bez strzelby — i trzej w jednej chwili
Jak gdyby na komendę razem wystrzelili.
Niedźwiedź wyskoczył w górę jak kot przed chartami
I głową na dół runął, i czterma łapami
Przewróciwszy się młyńcem, cielska krwawe brzemię
Waląc tuż pod Hrabiego, zbił go z nóg na ziemię.
Jeszcze ryczał, chciał jeszcze powstać, gdy nań wsiadły
Rozjuszona Strapczyna i Sprawnik zajadły. 
Natenczas Wojski chwycił na taśmie przypięty
Swój róg bawoli, długi, cętkowany, kręty
Jak wąż boa, oburącz do ust go przycisnął,
Wzdął policzki jak banię, w oczach krwią zabłysnął,
Zasunął wpół powieki, wciągnął w głąb pół brzucha
I do płuc wysłał z niego cały zapas ducha,
I zagrał: róg jak wicher wirowatym dechem,
Niesie w puszczę muzykę i podwaja echem.
Umilkli strzelcy, stali szczwacze zadziwieni
Mocą, czystością, dziwną harmoniją pieni.
Starzec cały kunszt, którym niegdyś w lasach słynął,
Jeszcze raz przed uszami myśliwców rozwinął;
Napełnił wnet, ożywił knieje i dąbrowy,
Jakby psiarnię w nie wpuścił i rozpoczął łowy.
Bo w graniu była łowów historyja krótka:
Zrazu odzew dźwięczący, rześki — to pobudka;
Potem jęki po jękach skomlą — to psów granie;
A gdzieniegdzie ton twardszy jak grzmot — to strzelanie.
Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało. 
Zadął znowu. Myśliłbyś, że róg kształty zmieniał
I że w ustach Wojskiego to grubiał, to cieniał,
Udając głosy zwierząt: to raz w wilczą szyję
Przeciągając się, długo, przeraźliwie wyje;
Znowu jakby w niedźwiedzie rozwarłszy się gardło,
Ryknął; potem beczenie żubra wiatr rozdarło.
Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało.
Wysłuchawszy rogowej arcydzieło sztuki,
Powtarzały je dęby dębom, bukom buki. 
Dmie znowu. Jakby w rogu były setne rogi,
Słychać zmieszane wrzaski szczwania, gniewu, trwogi,
Strzelców, psiarni i zwierząt; aż Wojski do góry
Podniósł róg i tryumfu hymn uderzył w chmury.
Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało.
Ile drzew, tyle rogów znalazło się w boru,
Jedne drugim pieśń niosą jak z choru do choru.
I szła muzyka coraz szersza, coraz dalsza,
Coraz cichsza i coraz czystsza, doskonalsza,
Aż znikła gdzieś daleko, gdzieś na niebios progu! 
Wojski obiedwie ręce odjąwszy od rogu
Rozkrzyżował; róg opadł, na pasie rzemiennym
Chwiał się. Wojski z obliczem nabrzmiałym, promiennym,
Z oczyma wzniesionymi, stał jakby natchniony,
Łowiąc uchem ostatnie znikające tony.
A tymczasem zagrzmiało tysiące oklasków,
Tysiące powińszowań i wiwatnych wrzasków.
Uciszono się z wolna i oczy gawiedzi
Zwróciły się na wielki, świeży trup niedźwiedzi.
Leżał krwią opryskany, kulami przeszyty,
Piersiami w gęszczę trawy wplątany i wbity;
Rozprzestrzenił szeroko przednie krzyżem łapy,
Dyszał jeszcze, wylewał strumień krwi przez chrapy,
Otwierał jeszcze oczy, lecz głowy nie ruszy;
Pijawki Podkomorzego dzierżą go pod uszy,
Z lewej strony Strapczyna, a z prawej zawisał
Sprawnik i dusząc gardziel krew czarną wysysał.
Za czym Wojski rozkazał kij żelazny włożyć
Psom między zęby i tak paszczęki roztworzyć.
Kolbami przewrócono na wznak zwierza zwłoki
I znów trzykrotny wiwat uderzył w obłoki. 
«A co? — krzyknął Asesor, kręcąc strzelby rurą —
A co? fuzyjka moja? górą nasi, górą!
A co? fuzyjka moja? niewielka ptaszyna,
A jak się popisała? To jej nie nowina:
Nie puści ona na wiatr żadnego ładunku.
Od książęcia Sanguszki mam ją w podarunku».
Tu pokazywał strzelbę przedziwnej roboty,
Choć maleńką, i zaczął wyliczać jej cnoty.
«Ja biegłem — przerwał Rejent, otarłszy pot z czoła —
Biegłem tuż za niedźwiedziem; a pan Wojski woła:
»Stój na miejscu!« Jak tam stać? Niedźwiedź w pole wali,
Rwąc z kopyta jak zając coraz daléj, daléj;
Aż mi ducha nie stało, dobiec ni nadziei,
Aż spojrzę w prawo: sadzi, a tu rzadko w kniei,
Jak też wziąłem na oko: postójże, marucha,
Pomyśliłem, i basta: ot, leży bez ducha!
Tęga strzelba, prawdziwa to Sagalasówka,
Napis: Sagalas London à Bałabanówka… 
(Sławny tam mieszka ślusarz Polak, który robił
Polskie strzelby, ale je po angielsku zdobił)».
«Jak to — parsknął Asesor — do kroćset niedźwiedzi!
To to niby pan zabił? Co też to Pan bredzi?»
«Słuchaj no — odparł Rejent — tu, panie, nie śledztwo,
Tu obława, tu wszystkich weźmiem na świadectwo…»
Więc kłótnia między zgrają wszczęła się zawzięta:
Ci stronę Asesora, ci brali Rejenta.
O Gerwazym nie wspomniał nikt, bo wszyscy biegli
Z boków i, co się z przodu działo, nie postrzegli.
Wojski głos zabrał: «Teraz jest przynajmniej za co;
Bo to, panowie, nie jest ów szarak ladaco,
To niedźwiedź; tu już nie żal poszukać odwetu,
Czy szerpentyną, czyli nawet z pistoletu.
Spór wasz trudno pogodzić, więc dawnym zwyczajem,
Na pojedynek nasze pozwolenie dajem.
Pamiętam, za mych czasów żyło dwóch sąsiadów,
Oba ludzie uczciwi, szlachta z prapradziadów,
Mieszkali po dwóch stronach nad rzeką Wilejką,
Jeden zwał się Domejko, a drugi Dowejko.
Do niedźwiedzicy oba razem wystrzelili:
Kto zabił, trudno dociec; strasznie się kłócili
I przysięgli strzelać się przez niedźwiedzią skórę:
To mi to po szlachecku, prawie rura w rurę.
Pojedynek ten wiele narobił hałasu;
Pieśni o nim śpiewano za owego czasu.
Ja byłem sekundantem; jak się wszystko działo,
Opowiem od początku historyję całą…» 
Nim Wojski zaczął mówić, Gerwazy spór zgodził.
On niedźwiedzia z uwagą dokoła obchodził,
Nareszcie dobył tasak, rozciął pysk na dwoje
I w tylcu głowy, mózgu rozkroiwszy słoje,
Znalazł kulę, wydobył, suknią ochędożył,
Przymierzył do ładunku, do flinty przyłożył,
A potem dłoń podnosząc i kulę na dłoni:
«Panowie — rzekł — ta kula nie jest z waszej broni,
Ona z tej Horeszkowskiej wyszła jednorurki
(Tu podniósł flintę starą, obwiązaną w sznurki),
Lecz nie ja wystrzeliłem. O, trzeba tam było
Odwagi; straszno wspomnieć, w oczach mi się ćmiło!
Bo prosto biegli ku mnie oba paniczowie,
A niedźwiedź z tyłu już, już na Hrabiego głowie,
Ostatniego z Horeszków!… chociaż po kądzieli.
»Jezus Maria!« krzyknąłem i Pańscy anieli
Zesłali mi na pomoc księdza bernardyna.
On nas wszystkich zawstydził; oj, dzielny księżyna!
Gdym drżał, gdym się do cyngla dotknąć nie ośmielił,
On mi z rąk flintę wyrwał, wycelił, wystrzelił:
Między dwie głowy strzelić! sto kroków! nie chybić!
I w sam środek paszczęki! tak mu zęby wybić!
Panowie! długo żyję: jednego widziałem
Człowieka, co mógł takim popisać się strzałem.
Ów głośny niegdyś u nas z tylu pojedynków,
Ów, co korki kobietom wystrzelał z patynków,
Ów łotr nad łotry, sławny w czasy wiekopomne,
Ów Jacek, vulgo Wąsal — nazwiska nie wspomnę…
Ale mu nie czas teraz dojeżdżać niedźwiedzi;
Pewnie po same wąsy hultaj w piekle siedzi.
Chwała księdzu! dwom ludziom on życie ocalił —
Może i trzem: Gerwazy nie będzie się chwalił,
Ale gdyby ostatnie z krwi Horeszków dziecię
Wpadło w bestyi paszczę, nie byłbym na świecie,
I moje by tam stare pogryzł niedźwiedź kości;
Pójdź, księże, wypijemy zdrowie jegomości».
Próżno szukano księdza; wiedzą tylko tyle,
Że po zabiciu źwierza zjawił się na chwilę,
Podskoczył ku Hrabiemu i Tadeuszowi,
A widząc, że obadwa cali są i zdrowi,
Podniósł ku niebu oczy, cicho pacierz zmówił
I pobiegł w pole szybko, jakby go kto łowił.
Tymczasem na Wojskiego rozkaz pęki wrzosu,
Suche chrusty i pniaki rzucono do stosu.
Bucha ogień, wyrasta szara sosna dymu,
I rozszerza się w górze na kształt baldakimu.
Nad płomieniem oszczepy złożono w koziołki,
Na grotach zawieszono brzuchate kociołki;
Z wozów niosą jarzyny, mąki i pieczyste,
I chleb.
Sędzia otworzył puzderko zamczyste,
W którym rzędami flaszek białe sterczą głowy;
Wybiera z nich największy kufel kryształowy
(Dostał go Sędzia w darze od księdza Robaka):
Wódka to gdańska, napój miły dla Polaka.
«Niech żyje — krzyknął Sędzia w górę wznosząc flaszę —
Miasto Gdańsk, niegdyś nasze, będzie znowu nasze!»
I lał srebrzysty likwor w kolej, aż na końcu
Zaczęło złoto kapać i błyskać na słońcu. 
W kociołkach bigos grzano. W słowach wydać trudno
Bigosu smak przedziwny, kolor i woń cudną;
Słów tylko brzęk usłyszy i rymów porządek,
Ale treści ich miejski nie pojmie żołądek.
Aby cenić litewskie pieśni i potrawy,
Trzeba mieć zdrowie, na wsi żyć, wracać z obławy. 
Przecież i bez tych przypraw potrawą nie lada
Jest bigos, bo się z jarzyn dobrych sztucznie składa.
Bierze się doń siekana, kwaszona kapusta,
Która, wedle przysłowia, sama idzie w usta;
Zamknięta w kotle, łonem wilgotnym okrywa
Wyszukanego cząstki najlepsze mięsiwa;
I praży się, aż ogień wszystkie z niej wyciśnie
Soki żywne, aż z brzegów naczynia war pryśnie
I powietrze dokoła zionie aromatem. 
Bigos już gotów. Strzelcy z trzykrotnym wiwatem,
Zbrojni łyżkami, biegą i bodą naczynie;
Miedź grzmi, dym bucha, bigos jak kamfora ginie;
Zniknął, uleciał; tylko w czeluściach saganów
Wre para jak w kraterze zagasłych wulkanów. 
Kiedy się już do woli napili, najedli,
Źwierza na wóz złożyli, sami na koń siedli,
Radzi wszyscy, rozmowni, oprócz Asesora
I Rejenta; ci byli gniewliwsi niż wczora,
Kłócąc się o zalety, ten swej Sanguszkówki,
A ten bałabanowskiej swej Sagalasówki.
Hrabia też i Tadeusz jadą nieweseli,
Wstydząc się, że chybili i że się cofnęli:
Bo na Litwie, kto źwierza wypuści z obławy,
Długo musi pracować, nim poprawi sławy.
Hrabia mówił, że pierwszy do oszczepu godził,
I że spotkaniu z źwierzem Tadeusz przeszkodził;
Tadeusz utrzymywał, że będąc silniejszy
I do robienia ciężkim oszczepem zręczniejszy,
Chciał wyręczyć Hrabiego: tak sobie niekiedy
Przemawiali śród gwaru i wrzasku czeredy.
Wojski jechał pośrodku; staruszek szanowny,
Wesoły był nadzwyczaj i bardzo rozmowny.
Chcąc kłótników zabawić i do zgody dowieść,
Kończył im o Doweyce i Domeyce powieść:
«Asesorze, jeżeli chciałem, byś z Rejentem
Pojedynkował, nie myśl, że jestem zawziętym
Na krew ludzką; broń Boże! Chciałem was zabawić,
Chciałem wam komedyję niby to wyprawić,
Wznowić koncept, który ja lat temu czterdzieście
Wymyśliłem — przedziwny! Wy młodzi jesteście,
Nie pamiętacie o nim; lecz za moich czasów,
Głośny był od tej puszczy do poleskich lasów.
Domeyki i Doweyki wszystkie sprzeciwieństwa
Pochodziły, rzecz dziwna, z nazwisk podobieństwa
Bardzo niewygodnego. Bo gdy w czas sejmików,
Przyjaciele Doweyki skarbili stronników,
Szepnął ktoś do szlachcica: »Daj kreskę Doweyce«.
A ten, nie dosłyszawszy, dał kreskę Domeyce.
Gdy na uczcie wniósł zdrowie marszałek Rupejko:
»Wiwat Doweyko!« — drudzy krzyknęli: »Domeyko!«
A kto siedział pośrodku, nie trafił do ładu,
Zwłaszcza przy niewyraźnej mowie w czas obiadu. 
Gorzej było. Raz w Wilnie jakiś szlachcic pjany
Bił się w szable z Domeyką i dostał dwie rany;
Potem ów szlachcic, z Wilna wracając do domu,
Dziwnym trafem z Doweyką zjechał się u promu.
Gdy więc na jednym promie płynęli Wilejką,
Pyta sąsiada, kto on? odpowie: Doweyko —
Nie czekając, dobywa rapier spod kirejki:
Czach, czach! i za Domeykę podciął wąs Doweyki.
Wreszcie, jak na dobitkę, trzeba jeszcze było,
Żeby na polowaniu tak się wydarzyło,
Że stali blisko siebie oba imiennicy,
I do jednej strzelili razem niedźwiedzicy.
Prawda, że po ich strzale upadła bez duchu;
Ale już pierwej niosła z dziesiątek kul w brzuchu.
Strzelby z jednym kalibrem miało wiele osób:
Kto zabił niedźwiedzicę? dojdźże! jaki sposób?
Tu już krzyknęli: »Dosyć! Trzeba raz rzecz skończyć,
Bóg nas czy diabeł złączył, trzeba się rozłączyć;
Dwóch nas jak dwóch słońc pono zanadto na świecie!«
A więc do szerpentynek i stają na mecie.
Oba szanowni ludzie; co ich szlachta godzą,
To oni na się jeszcze zapalczywiej godzą.
Zmienili broń: od szabel szło na pistolety;
Stają, krzyczym, że nadto przybliżyli mety;
Oni na złość, przysięgli przez niedźwiedzią skórę
Strzelać się: śmierć niechybna! prawie rura w rurę.
Oba tęgo strzelali — »Sekunduj, Hreczecha!«
»Zgoda — rzekłem — niech zaraz dół wykopie klecha:
Bo taki spór nie może skończyć się na niczym;
Lecz bijcie się szlacheckim trybem, nie rzeźniczym.
Dosyć już mety zbliżać, widzę, żeście zuchy;
Chcecie strzelać się, rury oparłszy na brzuchy?
Ja nie pozwolę. Zgoda, że na pistolety;
Lecz strzelać się nie z dalszej ani z bliższej mety,
Jak przez skórę niedźwiedzią. Ja rękami memi
Jako sekundant skórę rozciągnę na ziemi,
I ja sam was ustawię: Waść po jednej stronie
Stanie na końcu pyska, a Waść na ogonie«.
»Zgoda!« — wrzaśli; czas? — jutro; miejsce? — karczma Usza.
Rozjechali się. Ja zaś do Wirgilijusza…»
Tu Wojskiemu przerwał krzyk: «Wyczha!» Tuż spod koni
Smyknął szarak; już Kusy, już go Sokół goni.
Psy wzięto na obławę wiedząc, że z powrotem
Na polu łatwo można napotkać się z kotem;
Bez smyczy szły przy koniach; gdy kota spostrzegły,
Wprzód nim strzelcy poszczuli, już za nim pobiegły.
Rejent też i Asesor chcieli końmi natrzeć;
Lecz Wojski wstrzymał krzycząc: «Wara! stać i patrzeć!
Nikomu krokiem ruszyć z miejsca nie dozwolę;
Stąd widzim wszyscy dobrze, zając idzie w pole».
W istocie, kot czuł z tyłu myśliwych i psiarnie,
Rwał w pole, słuchy wytknął jak dwa różki sarnie,
Sam szarzał się nad rolą długi, wyciągnięty,
Skoki pod nim sterczały jakby cztery pręty,
Rzekłbyś, że ich nie rusza, tylko ziemię trąca
Po wierzchu, jak jaskółka wodę całująca.
Pył za nim, psy za pyłem; z daleka się zdało,
Że zając, psy i charty jedne tworzą ciało:
Jakby jakaś przez pole suwała się żmija,
Kot jak głowa, pył z tyłu jakby modra szyja,
A psami jak podwójnym ogonem wywija.
Rejent, Asesor patrzą, otworzyli usta,
Dech wstrzymali. Wtem Rejent pobladnął jak chusta,
Zbladł i Asesor; widzą… fatalnie się dzieje:
Owa żmija im dalej, tym bardziej dłużeje,
Już rwie się wpół, już znikła owa szyja pyłu,
Głowa już blisko lasu, ogony, gdzie z tyłu!
Głowa niknie; raz jeszcze jakby kto kutasem 
Mignął: w las wpadła; ogon urwał się pod lasem. 
Biedne psy, ogłupiałe, biegały pod gajem,
Zdawały się naradzać, oskarżać nawzajem.
Wreszcie wracają, z wolna skacząc przez zagony,
Spuściły uszy, tulą do brzucha ogony
I przybiegłszy, ze wstydu nie śmieją wznieść oczu,
I zamiast iść do panów, stały na uboczu. 
Rejent spuścił ku piersiom zasępione czoło,
Asesor rzucał okiem, ale niewesoło;
Potem zaczęli oba słuchaczom wywodzić:
Jak ich charty bez smycza nie nawykły chodzić,
Jak kot znienacka wypadł, jak źle był poszczuty
Na roli, gdzie psom chyba trzeba by wdziać buty,
Tak pełno wszędzie głazów i ostrych kamieni… 
Mądrze rzecz wyłuszczali szczwacze doświadczeni;
Myśliwi z tych mów wiele mogliby korzystać,
Lecz nie słuchali pilnie. Ci zaczęli świstać,
Ci śmiać się w głos, ci, mając niedźwiedzia w pamięci,
Gadali o nim, świeżą obławą zajęci.
Wojski ledwie raz okiem za zającem rzucił;
Widząc, że uciekł, głowę obojętnie zwrócił
I kończył rzecz przerwaną: «Na czym więc stanąłem?
Aha! na tym, że obu za słowo ująłem,
Iż będą strzelali się przez niedźwiedzią skórę…
Szlachta w krzyk: »To śmierć pewna! Prawie rura w rurę!«
A ja w śmiech. Bo mnie uczył mój przyjaciel Maro,
Że skóra zwierza nie jest lada jaką miarą.
Wszak wiecie waćpanowie, jak królowa Dydo 
Przypłynęła do Libów i tam z wielką biédą
Wytargowała sobie taki ziemi kawał,
Który by się wołową skórą nakryć dawał:
Na tym kawałku ziemi stanęła Kartago!
Więc ja to sobie w nocy rozbieram z uwagą.
Ledwie dniało, już z jednej strony taradejką 
Jedzie Doweyko, z drugiej na koniu Domeyko.
Patrzą, aż tu przez rzekę leży most kosmaty,
Pas ze skóry niedźwiedziej, porzniętej na szmaty.
Postawiłem Doweykę na źwierza ogonie
Z jednej strony, Domeykę zaś po drugiej stronie:
»Pukajcie teraz — rzekłem — choć przez całe życie,
Lecz póty was nie spuszczę, aż się pogodzicie«.
Oni w złość; a tu szlachta kładnie się na ziemi
Od śmiechu, a ja z księdzem słowy poważnemi
Nuż im z Ewangelii, z statutów dowodzić;
Nie ma rady: śmieli się i musieli zgodzić.
Spór ich potem w dozgonną przyjaźń się zamienił,
I Doweyko się z siostrą Domeyki ożenił;
Domeyko pojął siostrę szwagra, Doweykównę,
Podzielili majątek na dwie części równe,
A w miejscu, gdzie się zdarzył tak dziwny przypadek,
Pobudowawszy karczmę, nazwali Niedźwiadek». 
Księga piąta
Kłótnia
Plany myśliwskie Telimeny — Ogrodniczka wybiera się na wielki świat i słucha nauk opiekunki — Strzelcy wracają — Wielkie zadziwienie Tadeusza — Spotkanie się powtórne w Świątyni dumania i zgoda ułatwiona za pośrednictwem mrówek — U stołu wytacza się rzecz o łowach — Powieść Wojskiego o Rejtanie i księciu Denassów, przerwana — Zagajenie układów między stronami, także przerwane — Zjawisko z kluczem — Kłótnia — Hrabia z Gerwazym odbywają radę wojenną.

Wojski, chlubnie skończywszy łowy, wraca z boru,
A Telimena w głębi samotnego dworu
Zaczyna polowanie. Wprawdzie nieruchoma,
Siedzi z założonymi na piersiach rękoma,
Lecz myślą goni źwierzów dwóch; szuka sposobu,
Jak by razem obsaczyć i ułowić obu:
Hrabię i Tadeusza. Hrabia panicz młody,
Wielkiego domu dziedzic, powabnej urody,
Już trochę zakochany: cóż? może się zmienić!
Potem, czy szczerze kocha? czy się zechce żenić?
Z kobietą kilku laty starszą! niebogatą!
Czy mu krewni pozwolą? co świat powie na to? 
Telimena, tak myśląc, z sofy się podniosła
I stanęła na palcach: rzekłbyś, że podrosła;
Odkryła nieco piersi, wygięła się bokiem,
I sama siebie pilnym obejrzała okiem,
I znowu zapytała o radę zwierciadła;
Po chwili wzrok spuściła, westchnęła i siadła.
Hrabia pan! zmienni w gustach są ludzie majętni!
Hrabia blondyn… blondyni nie są zbyt namiętni!
A Tadeusz? prostaczek! poczciwy chłopczyna!
Prawie dziecko! raz pierwszy kochać się zaczyna!
Pilnowany, niełacno zerwie pierwsze związki;
Przy tym dla Telimeny ma już obowiązki…
Mężczyźni, póki młodzi, chociaż w myślach zmienni,
W uczuciach są od dziadów stalsi, bo sumienni.
Długo serce młodzieńca, proste i dziewicze,
Chowa wdzięczność za pierwsze miłości słodycze!
Ono rozkosz i wita, i żegna z weselem,
Jak skromną ucztę, którą dzielim z przyjacielem.
Tylko stary pjanica, gdy już spali trzewa,
Brzydzi się trunkiem, którym nazbyt się zalewa.
Wszystko to Telimena dokładnie wiedziała,
Bo i rozum, i wielkie doświadczenie miała.
Lecz co powiedzą ludzie?… Można im zejść z oczu,
W inne strony wyjechać, mieszkać na uboczu
Lub, co lepsza, wynieść się całkiem z okolicy,
Na przykład zrobić małą podróż do stolicy,
Młodego chłopca na świat wielki wyprowadzić,
Kroki jego kierować, pomagać mu, radzić,
Serce mu kształcić, mieć w nim przyjaciela, brata,
Nareszcie — użyć świata póki służą lata!… 
Tak myśląc, po alkowie śmiało i wesoło
Przeszła się kilka razy. Znów spuściła czoło. 
Warto by też pomyślić o Hrabiego losie…
Czyby się nie udało podsunąć mu Zosię?
Niebogata: lecz za to urodzeniem równa,
Z domu senatorskiego, jest dygnitarzówna.
Jeżeliby do skutku przyszło ożenienie,
Telimena w ich domu miałaby schronienie
Na przyszłość; krewna Zosi i Hrabiego swatka,
Dla młodego małżeństwa byłaby jak matka. 
Po tej z sobą odbytej, stanowczej naradzie,
Woła przez okno Zosię, bawiącą się w sadzie.
Zosia w porannym stroju i z głową odkrytą
Stała, trzymając w ręku podniesione sito;
Do nóg jej biegło ptastwo. Stąd kury szurpate
Toczą się kłębkiem; stamtąd kogutki czubate,
Wstrząsając koralowe na głowach szyszaki
I wiosłując skrzydłami przez bruzdy i krzaki,
Szeroko wyciągają ostrożaste pięty;
Za nimi z wolna indyk sunie się odęty
Sarkając na gderanie swej krzykliwej żony;
Ówdzie pawie jak tratwy długimi ogony
Sterują się po łące, a gdzieniegdzie z góry
Upada jak kiść śniegu gołąb srebrnopióry.
W pośrodku zielonego okręgu murawy,
Ściska się okrąg ptastwa, krzykliwy, ruchawy,
Opasany gołębi sznurem, na kształt wstęgi
Białej, środkiem pstrokaty w gwiazdy, w cętki, w pręgi.
Tu dzioby bursztynowe, tam czubki z korali
Wznoszą się z gęstwi pierza jak ryby spod fali,
Wysuwają się szyje i w ruchach łagodnych
Chwieją się ciągle na kształt tulipanów wodnych;
Tysiące oczu jak gwiazd błyskają ku Zosi.
Ona w środku wysoko nad ptastwem się wznosi;
Sama biała i w długą bieliznę ubrana
Kręci się, jak bijąca śród kwiatów fontanna;
Czerpie z sita i sypie na skrzydła i głowy,
Ręką jak perły białą, gęsty grad perłowy
Krup jęczmiennych. To ziarno godne pańskich stołów,
Robi się dla zaprawy litewskich rosołów;
Zosia je wykradając z szafy ochmistrzyni 
Dla swego drobiu, szkodę w gospodarstwie czyni.
Usłyszała wołanie: «Zosiu!» To głos cioci!
Sypnęła razem ptastwu ostatek łakoci,
A sama kręcąc sito, jako tanecznica
Bębenek, i w takt bijąc, swawolna dziewica
Jęła skakać przez pawie, gołębie i kury:
Zmieszane ptastwo tłumnie furknęło do góry.
Zosia, stopami ledwie dotykając ziemi,
Zdawała się najwyżej bujać między niemi;
Przodem gołębie białe, które w biegu płoszy,
Leciały jak przed wozem bogini rozkoszy. 
Zosia przez okno z krzykiem do alkowy wpadła,
I na kolanach ciotki zadyszana siadła;
Telimena, całując i głaszcząc pod brodę,
Z radością zważa dziecka żywość i urodę
(Bo prawdziwie kochała swą wychowanicę).
Ale znowu poważnie nastroiła lice,
Wstała i przechodząc się wszerz i wzdłuż alkowy,
Dzierżąc palec przy ustach, tymi rzekła słowy:
«Kochana Zosiu, już też całkiem zapominasz
I na stan, i na wiek twój: wszak to dziś zaczynasz
Rok czternasty. Czas rzucić indyki i kurki;
Fi! to godna zabawka dygnitarskiej córki!
I z umurzaną dziatwą chłopską już do woli
Napieściłaś się! Zosiu, patrząc serce boli:
Opaliłaś okropnie płeć, czysta Cyganka,
A chodzisz i ruszasz się jak parafijanka.
Już ja temu wszystkiemu na przyszłość zaradzę;
Od dziś zacznę, dziś ciebie na świat wyprowadzę,
Do salonu, do gości — gości mamy siła;
Patrzajżeż, ażebyś mnie wstydu nie zrobiła».
Zosia skoczyła z miejsca i klasnęła w dłonie,
I ciotce zawisnąwszy oburącz na łonie,
Płakała i śmiała się na przemian z radości.
«Ach ciociu, już tak dawno nie widziałam gości!
Od czasu, jak tu żyję z kury i indyki,
Jeden gość, co widziałam, to był gołąb dziki.
Już mi troszeczkę nudno tak siedzieć w alkowie;
Pan Sędzia nawet mówi, że to źle na zdrowie».
«Sędzia! — przerwała ciotka — ciągle mi dokuczał
Żeby cię na świat wywieść, ciągle pod nos mruczał
Że już jesteś dorosła: sam nie wie, co plecie,
Dziaduś, nigdy na wielkim niebywały świecie.
Ja wiem lepiej, jak długo trzeba się sposobić
Panience, by wyszedłszy na świat efekt zrobić.
Wiedz Zosiu, że kto rośnie na widoku ludzi,
Choć piękny, choć rozumny, efektów nie wzbudzi,
Gdy go wszyscy przywykną widzieć od maleńka;
Lecz niechaj ukształcona, dorosła panienka,
Nagle ni stąd, ni zowąd przed światem zabłyśnie,
Wtenczas każdy się do niej przez ciekawość ciśnie,
Wszystkie jej ruchy, rzuty oczu jej uważa,
Słowa jej podsłuchiwa i drugim powtarza;
A kiedy wejdzie w modę raz młoda osoba,
Każdy ją chwalić musi, choć i nie podoba.
Znaleźć się, spodziewam się, że umiesz: w stolicy
Urosłaś; choć dwa lata mieszkasz w okolicy,
Nie zapomniałaś jeszcze całkiem Petersburka.
No, Zosiu, toaletę rób, dostań tam z biurka,
Nagotowane znajdziesz wszystko do ubrania.
Spiesz się, bo lada chwila wrócą z polowania».
Wezwano pokojowę i służącą dziewkę,
W naczynie srebrne wody wylano konewkę.
Zosia, jak wróbel w piasku, trzepioce się, myje
Z pomocą sługi ręce, oblicze i szyję.
Telimena otwiera petersburskie składy,
Dobywa flaszki perfum, słoiki pomady,
Pokrapia Zosię wkoło wyborną perfumą,
(Woń napełniła izbę) włos namaszcza gumą.
Zosia kładnie pończoszki białe, ażurowe,
I trzewiki warszawskie białe, atłasowe.
Tymczasem pokojowa sznurowała stanik,
Potem rzuciła na gors pannie pudermanik;
Zaczęto przypieczone zbierać papiloty,
Pukle, że nazbyt krótkie, uwito w dwa sploty,
Zostawując na czole i skroniach włos gładki;
Pokojowa zaś świeżo zebrane bławatki
Uwiązawszy w plecionkę daje Telimenie,
Ta ją do głowy Zosi przyszpila uczenie,
Z prawej strony na lewo: kwiat od bladych włosów
Odbijał bardzo pięknie, jak od zboża kłosów!
Zdjęto puderman, całe ubranie gotowe.
Zosia białą sukienkę wrzuciła przez głowę,
Chusteczkę batystową białą w ręku zwija,
I tak cała wygląda biała jak lilija. 
Poprawiwszy raz jeszcze i włosów, i stroju,
Kazano jej wzdłuż i wszerz przejść się po pokoju.
Telimena uważa znawczyni oczyma,
Musztruje siostrzenicę, gniewa się i zżyma;
Aż na dygnienie Zosi krzyknęła z rozpaczy:
«Ja nieszczęśliwa! Zosiu, widzisz co to znaczy
Żyć z gęśmi, z pastuchami! Tak nogi rozszerzasz
Jak chłopiec, okiem w prawo i w lewo uderzasz,
Czysta rozwódka!… Dygnij, patrz, jaka niezwinna!» 
«Ach ciociu — rzekła smutnie Zosia — cóż ja winna!
Ciotka mnie zamykała; nie było z kim tańczyć,
Lubiłam z nudy ptastwo paść i dzieci niańczyć.
Ale poczekaj ciociu, niech no się pobawię
Trochę z ludźmi, obaczysz, jak się ja poprawię».
«Już — rzekła ciotka — z dwojga złego, lepiej z ptastwem,
Niż z tym, co u nas dotąd gościło plugastwem;
Przypomnij tylko sobie, kto tu u nas bywał:
Pleban, co pacierz mruczał lub w warcaby grywał,
I palestra z fajkami! To mi kawalery!
Nabrałabyś się od nich pięknej manijery.
Teraz to pokazać się jest przynajmniej komu,
Mamy przecież uczciwe towarzystwo w domu.
Uważaj dobrze, Zosiu, jest tu Hrabia młody,
Pan dobrze wychowany, krewny wojewody,
Pamiętaj być mu grzeczną».
Słychać rżenie koni
I gwar myśliwców; już są pod bramą: to oni!
Wziąwszy Zosię pod rękę pobiegła do sali.
Myśliwi na pokoje jeszcze nie wchadzali;
Musieli po komnatach odmieniać swą odzież,
Nie chcąc wniść do dam w kurtkach. Pierwsza wpadła młodzież,
Pan Tadeusz i Hrabia, co żywo przebrani. 
Telimena sprawuje obowiązki pani,
Wita wchodzących, sadza, rozmową zabawia,
I siostrzenicę wszystkim z kolei przedstawia:
Naprzód Tadeuszowi, jako krewną bliską.
Zosia grzecznie dygnęła, on skłonił się nisko,
Chciał coś do niej przemówić, już usta otworzył:
Ale spojrzawszy w oczy Zosi, tak się strwożył,
Że stojąc niemy przed nią, to płonął, to bladnął;
Co było w jego sercu, on sam nie odgadnął.
Uczuł się nieszczęśliwym bardzo — poznał Zosię!
Po wzroście i po włosach światłych, i po głosie;
Tę kibić i tę główkę widział na parkanie,
Ten wdzięczny głos zbudził go dziś na polowanie.
Aż Wojski Tadeusza wyrwał z zamięszania;
Widząc, że bladnie i że na nogach się słania,
Radził mu odejść do swej izby dla spoczynku.
Tadeusz stanął w kącie, wsparł się na kominku,
Nic nie mówiąc — szerokie, obłędne źrenice
Obracał to na ciotkę, to na siostrzenicę. 
Dostrzegła Telimena, iż pierwsze spojrzenie
Zosi tak wielkie na nim zrobiło wrażenie;
Nie odgadła wszystkiego, przecież pomięszana
Bawi gości, a z oczu nie spuszcza młodziana.
Wreszcie czas upatrzywszy ku niemu podbiega:
Czy zdrów? dlaczego smutny? pyta się, nalega,
Napomyka o Zosi, zaczyna z nim żarty;
Tadeusz nieruchomy, na łokciu oparty,
Nic nie gadając marszczył brwi i usta krzywił:
Tym bardziej Telimenę pomięszał i zdziwił.
Zmieniła więc natychmiast twarz i ton rozmowy,
Powstała zagniewana, i ostrymi słowy
Poczęła nań przymówki sypać i wyrzuty.
Porwał się i Tadeusz jak żądłem ukłuty,
Spojrzał krzywo, nie mówiąc ani słowa, splunął,
Krzesło nogą odepchnął i z pokoju runął,
Trzasnąwszy drzwi za sobą. Szczęściem, że tej sceny
Nikt z gości nie uważał oprócz Telimeny. 
Wyleciawszy przez bramę, biegł prosto na pole.
Jak szczupak, gdy mu oścień skróś piersi przekole,
Pluska się i nurtuje, myśląc że uciecze,
Ale wszędzie żelazo i sznur z sobą wlecze:
Tak i Tadeusz ciągnął za sobą zgryzoty,
Suwając się przez rowy i skacząc przez płoty,
Bez celu i bez drogi; aż niemało czasu
Nabłąkawszy się, w końcu wszedł w głębinę lasu
I trafił, czy umyślnie, czyli też przypadkiem,
Na wzgórek, co był wczora szczęścia jego świadkiem,
Gdzie dostał ów bilecik, zadatek kochania,
Miejsce, jak wiemy, zwane Świątynią dumania. 
Gdy okiem wkoło rzuca, postrzega: to ona!
Telimena, samotna, w myślach pogrążona,
Od wczorajszej postacią i strojem odmienna,
W bieliźnie, na kamieniu, sama jak kamienna;
Twarz schyloną w otwarte utuliła dłonie,
Choć nie słyszysz szlochania, znać, że we łzach tonie. 
Daremnie broniło się serce Tadeusza;
Ulitował się, uczuł że go żal porusza.
Długo poglądał niemy, ukryty za drzewem,
Na koniec westchnął i rzekł sam do siebie z gniewem:
«Głupi! cóż ona winna, że się ja pomylił?»
Więc z wolna głowę ku niej zza drzewa wychylił — 
Gdy nagle Telimena zrywa się z siedzenia,
Rzuca się w prawo, w lewo, skacze skróś strumienia,
Rozkrzyżowana, z włosem rozpuszczonym, blada,
Pędzi w las, podskakuje, przyklęka, upada,
I nie mogąc już powstać, kręci się po darni;
Widać z jej ruchów, w jakiej strasznej jest męczarni:
Chwyta się za pierś, szyję, za stopy, kolana.
Skoczył Tadeusz myśląc, że jest pomieszana 
Lub ma wielką chorobę. Lecz z innej przyczyny
Pochodziły te ruchy.
U bliskiej brzeziny
Było wielkie mrowisko. Owad gospodarny
Snuł się wkoło po trawie, ruchawy i czarny.
Nie wiedzieć, czy z potrzeby czy z upodobania,
Lubił szczególnie zwiedzać Świątynię dumania;
Od stołecznego wzgórka aż po źródła brzegi
Wydeptał drogę, którą wiódł swoje szeregi.
Nieszczęściem, Telimena siedziała śród drożki:
Mrówki, znęcone blaskiem bieluchnej pończoszki,
Wbiegły, gęsto zaczęły łaskotać i kąsać,
Telimena musiała uciekać, otrząsać,
Na koniec na murawie siąść i owad łowić. 
Nie mógł jej swej pomocy Tadeusz odmówić:
Oczyszczając sukienkę, aż do nóg się zniżył,
Usta trafem ku skroniom Telimeny zbliżył —
W tak przyjaznej postawie, choć nic nie mówili
O rannych kłótniach swoich, przecież się zgodzili;
I nie wiedzieć, jak długo trwałaby rozmowa,
Gdyby ich nie przebudził dzwonek z Soplicowa —
Hasło wieczerzy.
Pora powracać do domu,
Zwłaszcza że słychać było opodal trzask łomu.
Może szukają? razem wracać nie wypada;
Więc Telimena w prawo pod ogród się skrada,
A Tadeusz na lewo biegł do wielkiej drogi.
Oboje w tym odwrocie mieli nieco trwogi:
Telimenie zdało się, że raz spoza krzaka
Błysła zakapturzona, chuda twarz Robaka;
Tadeusz widział dobrze, jak mu raz i drugi
Pokazał się na lewo cień biały i długi,
Co to było, nie wiedział, ale miał przeczucie,
Że to był Hrabia w długim, angielskim surducie. 
Wieczerzano w zamczysku. Uparty Protazy,
Nie dbając na wyraźne Sędziego zakazy,
W niebytność państwa znowu do zamku szturmował,
I kredens doń (jak mówi) zaintromitował.
Goście weszli w porządku i stanęli kołem;
Podkomorzy najwyższe brał miejsce za stołem:
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się damom, starcom i młodzieży;
Kwestarz nie był u stołu; miejsce bernardyna,
Po prawej stronie męża, ma Podkomorzyna,
Sędzia, kiedy już gości jak trzeba ustawił,
Żegnając po łacinie, stół pobłogosławił.
Mężczyznom dano wódkę; za czym wszyscy siedli,
I chłodnik zabielany milcząc żwawo jedli.
Po chłodniku szły raki, kurczęta, szparagi,
W towarzystwie kielichów węgrzyna, malagi.
Jedzą, piją, a milczą wszyscy. Nigdy pono,
Od czasu jako mury zamku podźwigniono,
Który uraczał hojnie tylu szlachty bratów,
Tyle wesołych słyszał i odbił wiwatów,
Nie pamiętano takiej posępnej wieczerzy;
Tylko pukanie korków i brzęki talerzy,
Odbijała zamkowa sień wielka i pusta:
Rzekłbyś, iż zły duch gościom zasznurował usta. 
Mnogie były powody milczenia. Myśliwi
Powrócili z ostępu dosyć gadatliwi,
Lecz gdy zapał ochłonął, myśląc nad obławą,
Postrzegają, że wyszli z niej z niewielką sławą:
Trzebaż było, ażeby jeden kaptur popi,
Wyrwawszy się Bóg wie skąd, jak Filip z konopi,
Przepisał wszystkich strzelców powiatu? O wstydzie!
Cóż o tym będą gadać w Oszmianie i Lidzie,
Które od wieków walczą z tutejszym powiatem
O pierwszeństwo w strzelectwie? Myślili więc nad tem.
Zaś Asesor i Rejent, prócz wspólnych niechęci,
Świeżą hańbę swych chartów mieli na pamięci.
W oczach im stoi niecny kot: skoki wyciąga,
I omykiem spod gaju kiwając urąga,
I tym omykiem ćwiczy po sercach jak biczem…
Siedzieli z pochylonym ku misie obliczem.
Asesor nowe jeszcze miał powody żalów,
Patrząc na Telimenę i na swych rywalów.
Do Tadeusza siedzi Telimena bokiem,
Pomięszana, zaledwie śmie nań rzucić okiem;
Chciała zasępionego Hrabiego zabawić,
Wyzwać w dłuższą rozmowę, w lepszy humor wprawić;
Bo Hrabia dziwnie kwaśny powrócił z przechadzki
A raczej, jako myślił Tadeusz, z zasadzki.
Słuchając Telimeny, czoło podniósł hardo,
Brwi zmarszczył, spojrzał na nią ledwie nie z pogardą;
Potem przysiadł się, jak mógł najbliżej, do Zosi,
Nalewa jej do szklanki, talerze przynosi,
Prawi tysiąc grzeczności, kłania się, uśmiécha,
Czasem oczy wywraca i głęboko wzdycha.
Widać przecież, pomimo tak zręczne łudzenie,
Że umizgał się tylko na złość Telimenie:
Bo głowę odwracając, niby nieumyślnie,
Coraz ku Telimenie groźnym okiem błyśnie. 
Telimena nie mogła pojąć, co to znaczy;
Ruszywszy ramionami, myśliła: dziwaczy!
Wreszcie nowym zalotom Hrabiego dość rada,
Zwróciła się do swego drugiego sąsiada. 
Tadeusz też posępny, nic nie jadł, nic nie pił,
Zdawał się słuchać rozmów, oczy w talerz wlepił;
Telimena mu leje wino, on się gniewa
Na natrętność; pytany o zdrowie — poziewa.
Ma za złe (tak się zmienił jednego wieczora),
Że Telimena zbytnie do zalotów skora;
Gorszy się, że jej suknia tak wcięta głęboko,
Nieskromnie — a dopiero, kiedy podniósł oko!
Aż przeląkł się; bystrzejsze teraz miał źrenice.
Ledwie spojrzał w rumiane Telimeny lice,
Odkrył od razu wielką, straszną tajemnicę —
Przebóg! naróżowana!
Czy róż w złym gatunku,
Czy jakoś na obliczu przetarł się z trafunku:
Gdzieniegdzie zrzedniał, na wskroś grubszą płeć odsłania…
Może to sam Tadeusz, w Świątyni dumania,
Rozmawiając za blisko, omusknął z bielidła
Karmin lżejszy od pyłków motylego skrzydła;
Telimena wracała nazbyt śpieszno z lasu,
I poprawić kolory swe nie miała czasu:
Około ust szczególnie widne były piegi.
Nuż oczy Tadeusza, jako chytre szpiegi,
Odkrywszy jedną zdradę, poczną w kolej zwiedzać
Resztę wdzięków i wszędzie jakiś fałsz wyśledzać:
Dwóch zębów brakuje w ustach; na czole, na skroni
Zmarszczki; tysiąc zmarszczków pod brodą się chroni!
Niestety! Czuł Tadeusz, jak jest niepotrzebnie
Rzecz piękną nazbyt ściśle zważać; jak haniebnie,
Być szpiegiem swej kochanki; nawet jak szkaradnie,
Odmieniać smak i serce — lecz któż sercem władnie?
Darmo chce brak miłości zastąpić sumnieniem,
Chłód duszy ogrzać znowu jej wzroku promieniem:
Już ten wzrok, jako księżyc światły a bez ciepła,
Błyskał po wierzchu duszy, która do dna krzepła. 
Takie robiąc sam w sobie wyrzuty i skargi,
Pochylił w talerz głowę, milczał i gryzł wargi. 
Tymczasem zły duch nową pokusą go wabi,
Podsłuchiwać, co Zosia mówiła do Hrabi.
Dziewczyna, uprzejmością Hrabiego ujęta,
Zrazu rumieniła się, spuściwszy oczęta,
Potem śmiać się zaczęli, w końcu rozmawiali
O jakimś niespodzianym w ogrodzie spotkaniu,
O jakimś po łopuchach i grzędach stąpaniu,
Tadeusz, wyciągnąwszy co najdłużej uszy,
Połykał gorzkie słowa i przetrawiał w duszy.
Okropną miał biesiadę. Jak w ogrodzie żmija
Dwoistym żądłem zioło zatrute wypija,
Potem skręci się w kłębek i na drodze legnie,
Grożąc stopie, co na nią nieostrożnie biegnie:
Tak Tadeusz, opiły trucizną zazdrości,
Zdawał się obojętny, a pękał ze złości. 
W najweselszym zebraniu, niech się kilku gniewa,
Zaraz się ich ponurość na resztę rozlewa:
Strzelcy dawniej milczeli; druga stołu strona
Umilkła, Tadeusza żółcią zarażona. 
Nawet pan Podkomorzy nadzwyczaj ponury,
Nie miał ochoty gadać, widząc swoje córy,
Posażne i nadobne panny, w wieku kwiecie,
Zdaniem wszystkich najpierwsze partyje w powiecie,
Milczące, zaniedbane od milczącej młodzi.
Gościnnego Sędziego również to obchodzi;
Wojski zaś, uważając że tak wszyscy milczą,
Nazywał tę wieczerzę nie polską, lecz wilczą.
Hreczecha na milczenie miał słuch bardzo czuły.
Sam gawęda, i lubił niezmiernie gaduły.
Nie dziw! Ze szlachtą strawił życie na biesiadach,
Na polowaniach, zjazdach, sejmikowych radach:
Przywykł, żeby mu zawsze coś bębniło w uchu,
Nawet wtenczas, gdy milczał lub z placką za muchą
Skradał się, lub zamknąwszy oczy siadał marzyć;
W dzień szukał rozmów, w nocy musiano mu gwarzyć
Pacierze różańcowe albo gadać bajki.
Stąd też nieprzyjacielem zabitym był fajki,
Wymyślonej od Niemców, by nas zcudzoziemczyć;
Mawiał: Polskę oniemić, jest to Polskę zniemczyć.
Starzec, wiek przegwarzywszy, chciał spoczywać w gwarze;
Milczenie go budziło ze snu: tak młynarze,
Uśpieni kół turkotem, ledwie staną osie,
Budzą się krzycząc z trwogą: «A słowo stało się…» 
Wojski ukłonem dawał znak Podkomorzemu,
A ręką od ust lekko skinął ku Sędziemu,
Prosząc o głos. Panowie na ten ukłon niemy
Odkłonili się oba, co znaczy: prosiemy.
Wojski zagaił. 
«Śmiałbym upraszać młodzieży,
Ażeby po staremu bawić u wieczerzy,
Nie milczeć i żuć: czy my ojce kapucyni?
Kto milczy między szlachtą, to właśnie tak czyni,
Jako myśliwiec, który nabój rdzawi w strzelbie.
Dlatego ja rozmowność naszych przodków wielbię:
Po łowach szli do stołu, nie tylko by jadać,
Ale aby nawzajem mogli się wygadać,
Co każdy miał na sercu; nagany, pochwały
Strzelców i obławników, ogary, wystrzały
Wywoływano na plac; powstawała wrzawa,
Miła uchu myśliwców jak druga obława. 
Wiem, wiem, o co wam idzie. Ta czarnych trosk chmura
Pono z Robakowego wzniosła się kaptura!
Wstydzicie się swych pudeł! Niech was wstyd nie pali:
Znałem myśliwych lepszych od was, a chybiali;
Trafiać, chybiać, poprawiać, to kolej strzelecka.
Ja sam, chociaż ze strzelbą włóczę się od dziecka,
Chybiałem; chybiał sławny ów strzelec Tułoszczyk,
Nawet nie zawsze trafiał pan Rejtan nieboszczyk.
O Rejtanie opowiem później. Co się tycze
Wypuszczenia z obławy, że oba panicze
Zwierzowi jak należy kroku nie dostali,
Choć mieli oszczep w ręku: tego nikt nie chwali
Ani gani. Bo zmykać, mając nabój w rurze,
Znaczyło po staremu być tchórzem nad tchórze;
Toż wystrzelić na oślep (jak to robi wielu),
Nie przypuściwszy źwierza, nie wziąwszy do celu,
Jest rzecz haniebna; ale kto dobrze wymierzy,
Kto przypuści do siebie źwierza jak należy,
Jeśli chybił, cofnąć się może bez sromoty,
Albo walczyć oszczepem — lecz z własnej ochoty,
A nie z musu: gdyż oszczep strzelcom poruczony
Nie dla natarcia, ale tylko dla obrony. 
Tak było po staremu. A więc mnie zawierzcie,
I waszej rejterady do serca nie bierzcie,
Kochany Tadeuszku i wielmożny grafie;
Ilekroć zaś wspomnicie o dzisiejszym trafie,
Wspomnijcie też starego Wojskiego przestrogę:
Nigdy jeden drugiemu nie zachodzić w drogę,
Nigdy we dwóch nie strzelać do jednej źwierzyny».
Właśnie Wojski wymawiał to słowo: źwierzyny,
Gdy Asesor półgębkiem podszepnął: dziewczyny;
«Brawo!» krzyknęła młodzież, powstał szmer i śmiechy;
Powtarzano z kolei przestrogę Hreczechy,
Mianowicie ostatnie słowo; ci źwierzyny,
A drudzy, w głos śmiejąc się, krzyczeli: dziewczyny.
Rejent szepnął: kobiety, Asesor: kokiety,
Utkwiwszy w Telimenie oczy jak sztylety. 
Nie myślił wcale Wojski przymawiać nikomu,
Ani uważał, co tam szepczą po kryjomu;
Rad bardzo, że mógł damy i młodzież rozśmieszyć,
Zwrócił się ku myśliwcom, chcąc i tych pocieszyć;
I zaczął, nalewając sobie kielich wina:
«Nadaremnie oczyma szukam bernardyna;
Chciałbym mu opowiedzieć wypadek ciekawy,
Podobny do zdarzenia dzisiejszej obławy.
Klucznik mówił, że tylko znał jednego człeka,
Co tak celnie jak Robak mógł strzelić z daleka;
Ja zaś znałem drugiego: równie trafnym strzałem
Ocalił on dwóch panów; sam ja to widziałem,
Kiedy do nalibockich zaciągnęli lasów
Tadeusz Rejtan poseł i książę Denassów.
Nie zazdrościli sławie szlachcica panowie;
Owszem, u stołu pierwsi wnieśli jego zdrowie,
Nadawali mu wielkich prezentów bez liku,
I skórę zabitego dzika. O tym dziku
I o strzale, powiem wam jak naoczny świadek:
Bo to był dzisiejszemu podobny przypadek,
A zdarzył się największym strzelcom za mych czasów,
Posłowi Rejtanowi i księciu Denassów».
A wtem ozwał się Sędzia nalewając czaszę:
«Piję zdrowie Robaka, Wojski, w ręce wasze!
Jeśli datkiem nie możem kwestarza zbogacić,
Postaramy się przecież za proch mu zapłacić:
Uręczamy, że niedźwiedź zabity dziś w boru
Przez dwa lata wystarczy na kuchnię klasztoru.
Lecz skóry księdzu nie dam: lub gwałtem zabiorę,
Albo ją mnich ustąpić musi przez pokorę,
Albo ją kupię choćby dziesiątkiem soboli.
Skórą tą rozrządzimy wedle naszej woli:
Pierwszy wieniec i sławę już wziął sługa boży;
Skórę jaśnie wielmożny pan nasz Podkomorzy
Temu da, kto na drugą nagrodę zasłużył».
Podkomorzy pogładził czoło i brwi zmrużył;
Strzelcy zaczęli szemrać, każdy coś powiadał:
Tamten jak źwierza znalazł, ten jak ranę zadał,
Tamten psiarnię zawołał, ów źwierza nawrócił
Znowu w ostęp. Asesor z Rejentem się kłócił,
Jeden wielbiąc przymioty swojej Sanguszkówki,
Drugi bałabanowskiej swej Sagalasówki.
«Sędzio sąsiedzie — wreszcie wyrzekł Podkomorzy —
Pierwszą nagrodę słusznie zyskał sługa boży;
Lecz niełacno rozsądzić, kto jest po nim drugi,
Bo wszyscy zdają mi się mieć równe zasługi,
Wszyscy równi zręcznością, biegłością i męstwem.
Przecież dwóch dziś odznaczył los niebezpieczeństwem.
Dwaj byli niedźwiedziego najbliżsi pazura:
Tadeusz i pan Hrabia; im należy skóra.
Pan Tadeusz ustąpi (jestem tego pewny),
Jako młodszy i jako gospodarza krewny;
Więc spolia opima weźmiesz, mości Hrabia:
Niech ten łup twą strzelecką komnatę ozdabia,
Niechaj pamiątką będzie dzisiejszej zabawy,
Godłem szczęścia łowczego, bodźcem przyszłej sławy».
Umilknął wesół, myśląc, że Hrabię ucieszył;
Nie wiedział, jak boleśnie serce jego przeszył.
Bo Hrabia, na strzeleckiej komnaty wspomnienie,
Mimowolnie wzrok podniósł: a te łby jelenie,
Te gałęziste rogi, jakby las wawrzynów
Zasiany ręką ojców na wieńce dla synów,
Te rzędami portretów zdobione filary,
Ten w sklepieniu błyszczący herb Półkozic stary,
Ozwały się doń zewsząd głosami przeszłości.
Zbudził się z marzeń, wspomniał gdzie, u kogo gości:
Dziedzic Horeszków, gościem śród swych własnych progów,
Biesiadnikiem Sopliców, swych odwiecznych wrogów!
A przy tym zawiść, którą czuł dla Tadeusza,
Tym mocniej Hrabię przeciw Soplicom porusza.
Rzekł więc z gorzkim uśmiechem: «Mój domek zbyt mały,
Nie ma godnego miejsca na dar tak wspaniały;
Niech lepiej niedźwiedź czeka pośród tych rogaczy,
Aż mi go Sędzia razem z zamkiem oddać raczy». 
Podkomorzy zgadując, na co się zanosi,
Zadzwonił w tabakierkę złotą, o głos prosi.
«Godzieneś pochwał — rzecze — Hrabio, mój sąsiedzie,
Że dbasz o interesa nawet przy obiedzie,
Nie tak jak modni wieku twojego panicze,
Żyjący bez rachunku. Ja tuszę i życzę
Zgodą zakończyć moje sądy podkomorskie.
Dotąd jedyna trudność jest o fundum dworskie:
Mam już projekt zamiany, fundum wynagrodzić
Ziemią, w sposób następny…» Tu zaczął wywodzić
Porządnie (jak zwykł zawsze) plan przyszłej zamiany.
Już był w połowie rzeczy: gdy ruch niespodziany
Wszczął się na końcu stoła. Jedni coś postrzegli,
Wskazują palcem; drudzy oczyma tam biegli,
Aż wreszcie wszystkie głowy, jak kłosy schylone
Wstecznym wiatrem, w przeciwną zwróciły się stronę
W kąt.
Z kąta, kędy wisiał portret nieboszczyka,
Ostatniego z rodziny Horeszków Stolnika,
Z małych drzwiczek, ukrytych pomiędzy filary,
Wysunęła się cicho postać, na kształt mary:
Gerwazy; poznano go po wzroście, po licach,
Po srebrzystych na żółtej kurcie Półkozicach.
Stąpał jako słup prosto, niemy i surowy,
Nie zdjąwszy czapki, nawet nie schyliwszy głowy;
W ręku trzymał błyszczący klucz jakby puginał,
Odemknął szafę i w niej coś kręcić zaczynał.
Stały w dwóch kątach sieni, wsparte o filary,
Dwa kurantowe, w szafach zamknięte zegary;
Dziwaki stare, dawno ze słońcem w niezgodzie,
Południe wskazywały często o zachodzie. 
Gerwazy nie przybrał się machiny naprawić,
Ale bez nakręcenia nie chciał jej zostawić:
Dręczył kluczem zegary każdego wieczora;
Właśnie teraz przypadła nakręcania pora.
Gdy Podkomorzy sprawą zajmował uwagę
Stron interesowanych, on pociągnął wagę:
Zgrzytnęły wyszczerbionym zębem koła rdzawe,
Wzdrygnął się Podkomorzy i przerwał rozprawę.
«Bracie — rzekł — odłóż nieco twą pilną robotę»
I kończył plan zamiany. Lecz Klucznik na psotę
Jeszcze silniej pociągnął drugiego ciężaru;
I wnet gil, który siedział na wierzchu zegaru,
Trzepiocąc skrzydłem zaczął ciąć kurantów nuty.
Ptak sztucznie wyrobiony, szkoda, że zepsuty,
Ząjąkał się i piszczał, im dalej, tym gorzéj.
Goście w śmiech; musiał przerwać znowu Podkomorzy.
«Mości Kluczniku — krzyknął — lub raczej puszczyku,
Jeśli dziób twój szanujesz, dość mi tego krzyku».
Ale Gerwazy groźbą wcale się nie strwożył;
Prawą rękę poważnie na zegar położył,
A lewą wziął się pod bok. Tak oburącz wsparty,
«Podkomorzeńku! — krzyknął — wolne pańskie żarty,
Wróbel mniejszy niż puszczyk, a na swoich wiorach
Śmielszy jest aniżeli puszczyk w cudzych dworach:
Co Klucznik to nie puszczyk; kto w cudze poddasze
Nocą włazi, ten puszczyk, i ja go wystraszę».
«Za drzwi z nim!» Podkomorzy krzyknął.
«Panie Hrabia! —
Zawołał Klucznik — widzisz pan, co się wyrabia.
Czy nie dosyć się jeszcze pański honor plami,
Że pan jadasz i pijasz z tymi Soplicami;
Trzebaż jeszcze, aby mnie, zamku urzędnika,
Gerwazego Rembajłę, Horeszków Klucznika,
Lżyć w domu panów moich? i panże to zniesie!» 
Wtem Protazy zawołał trzykroć: «Uciszcie się!
Na ustęp! Ja, Protazy Baltazar Brzechalski,
Dwojga imion, generał niegdyś trybunalski,
Vulgo Woźny, woźnieńską obdukcyją robię
I wizyją formalną, zamawiając sobie
Urodzonych tu wszystkich obecnych świadectwo,
I pana Asesora wzywając na śledztwo,
Z powodu wielmożnego Sędziego Soplicy:
O inkursyją, to jest o najazd granicy,
Gwałt zamku, w którym Sędzia dotąd prawnie włada,
Czego dowodem jawnym jest, że w zamku jada».
«Brzechaczu! — wrzasnął Klucznik — ja cię wnet nauczę!»
I dobywszy zza pasa swe żelazne klucze,
Okręcił wkoło głowy, puścił z całej mocy.
Pęk żelaza wyleciał jako kamień z procy,
Pewnie łeb Protazemu rozbiłby na ćwierci;
Szczęściem, schylił się Woźny i wydarł się śmierci.
Porwali się z miejsc wszyscy; chwilę była głucha
Cichość, aż Sędzia krzyknął: «W dyby tego zucha!
Hola, chłopcy!» — i czeladź rzuciła się żwawo
Ciasnym przejściem pomiędzy ścianami i ławą.
Lecz Hrabia krzesłem w środku zagrodził im drogę
I na tym szańcu słabym utwierdziwszy nogę,
«Wara! — zawołał — Sędzio! nie wolno nikomu
Krzywdzić sługę mojego w moim własnym domu:
Kto ma na starca skargę, niech mi ją przełoży».
Zyzem w oczy Hrabiemu spojrzał Podkomorzy:
«Bez waścinej pomocy ukarać potrafię
Zuchwałego szlachetkę; a waść, mości grafie,
Przed dekretem ten zamek za wcześnie przywłaszczasz:
Nie wać tu jesteś panem, nie wać nas ugaszczasz.
Siedź cicho, jakeś siedział; jeśli siwej głowy
Nie czcisz, to szanuj pierwszy urząd powiatowy».
«Co mi? — odmruknął Hrabia — dość już tej gawędy;
Nudźcie drugich waszymi względy i urzędy! 
Dość już głupstwa zrobiłem, wdając się z waćpaństwem
W pijatyki, które się kończą grubijaństwem;
Zdacie mi sprawę z mego honoru obrazy.
Do widzenia po trzeźwu; pójdź za mną, Gerwazy!» 
Nigdy się odpowiedzi takiej nie spodziewał
Podkomorzy. Właśnie swój kieliszek nalewał;
Gdy zuchwalstwem Hrabiego rażony jak gromem,
Oparłszy się o kielich butlem nieruchomym,
Głowę wyciągnął na bok i ucha przyłożył,
Oczy rozwarł szeroko, usta wpół otworzył;
Milczał, lecz kielich w ręku tak potężnie cisnął,
Że szkło dźwięknąwszy pękło, płyn w oczy mu prysnął.
Rzekłbyś, że z winem ognia w duszę się nalało:
Tak oblicze spłonęło, tak oko pałało. 
Zerwał się mówić; pierwsze słowo niewyraźnie
Mleł w ustach; aż przez zęby wyleciało: «Błaźnie!
Grafiątko! ja cię! Tomasz, karabelę! Ja tu
Nauczę ciebie mores, błaźnie, daj go katu!
Względy, urzędy nudzą, uszko delikatne!
Ja cię tu zaraz po tych zauszniczkach płatnę.
Fora za drzwi! Do korda! Tomasz, karabelę!»
Wtem do Podkomorzego skoczą przyjaciele;
Sędzia porwał mu rękę: «Stój pan, to rzecz nasza,
Mnie tu naprzód wyzwano. Protazy, pałasza!
Puszczę go w taniec jako niedźwiadka na kiju».
Lecz Tadeusz Sędziego wstrzymał: «Panie stryju,
Wielmożny Podkomorzy, czyż się państwu godzi
Wdawać się z tym fircykiem; czy tu nie ma młodzi?
Na mnie to zdajcie: ja go należycie skarcę.
A waszeć, panie śmiałku, co wyzywasz starce,
Obaczym, czyli jesteś tak strasznym rycerzem:
Rozprawimy się jutro, plac i broń wybierzem;
Dziś uchodź, pókiś cały». 
Dobra była rada:
Klucznik i Hrabia wpadli w obroty nie lada.
Przy wyższym końcu stoła wrzał tylko krzyk wielki,
Ale z ostrego końca latały butelki
Koło Hrabiego głowy. Strwożone kobiety
W prośby, w płacz; Telimena, krzyknąwszy: «Niestety!»
Wzniosła oczy, powstała, i padła zemdlona,
I przechyliwszy szyję przez Hrabi ramiona,
Na pierś jego złożyła swe piersi łabędzie.
Hrabia, choć zagniewany, wstrzymał się w zapędzie,
Zaczął cucić, ocierać.
Tymczasem Gerwazy,
Wystawiony na stołków i butelek razy,
Już zachwiał się, już czeladź zakasawszy pięście
Rzucała się nań zewsząd hurmem: gdy na szczęście
Zosia, widząc szturm, skoczy, i litością zdjęta
Zasłania starca, na krzyż rozpiąwszy rączęta.
Wstrzymali się; Gerwazy z wolna ustępował,
Zniknął z oczu, szukano, gdzie się pod stół schował:
Gdy nagle, z drugiej strony, wyszedł jak spod ziemi,
Podniósłszy w górę ławę ramiony silnemi,
Okręcił się jak wiatrak, oczyścił pół sieni,
Wziął Hrabię; i tak oba, ławą zasłonieni,
Cofali się ku drzwiczkom; już dochodzą progów:
Gerwazy stanął, jeszcze raz spojrzał na wrogów.
Dumał chwilę, niepewny, czy cofać się zbrojnie,
Czyli z nowym orężem szukać szczęścia w wojnie:
Obrał drugie. Już ławę jak taran murowy
W tył dźwignął dla zamachu; już ugiąwszy głowy,
Z wypiętą na przód piersią, z podniesioną nogą,
Miał wpaść… ujrzał Wojskiego, uczuł w sercu trwogę.
Wojski, cicho siedzący z przymrużonym okiem,
Zdawał się pogrążony w dumaniu głębokiem.
Dopiero, gdy się Hrabia z Podkomorzym skłócił:
I Sędziemu pogroził, Wojski głowę zwrócił,
Zażył dwakroć tabaki i przetarł powieki.
Chociaż Wojski Sędziemu był krewny daleki,
Ale w gościnnym jego domu zamieszkały,
O zdrowie przyjaciela był niezmiernie dbały.
Przypatrywał się zatem z ciekawością walce;
Wyciągnął z lekka na stół rękę, dłoń i palce,
Położył nóż na dłoni, trzonkiem do paznokcia
Indeksu, a żelazem zwrócony do łokcia;
Potem rękę w tył nieco wychyloną kiwał,
Niby bawiąc się: lecz się w Hrabiego wpatrywał.
Sztuka rzucania nożów, straszna w ręcznej bitwie,
Już była zaniedbana podówczas na Litwie,
Znajoma tylko starym; Klucznik jej próbował
Nieraz w zwadach karczemnych, Wojski w niej celował:
Widać z zamachu ręki, że silnie uderzy,
A z oczu łacno zgadnąć, że w Hrabiego mierzy
(Ostatniego z Horeszków, chociaż po kądzieli),
Mniej baczni młodzi ruchów starca nie pojęli:
Gerwazy zbladnął, ławą Hrabiego zakłada,
Cofa się ku drzwiom. «Łapaj!» krzyknęła gromada.
Jako wilk, obskoczony znienacka przy ścierwie,
Rzuca się oślep w zgraję, co mu ucztę przerwie;
Już goni, ma ją szarpać: wtem śród psiego wrzasku
Trzasło ciche półkurcze; wilk zna je po trzasku,
Śledzi okiem, postrzega, że z tyłu, za charty,
Myśliwiec wpół schylony, na kolanie wsparty,
Rurą ku niemu wije i już cyngla tyka.
Wilk uszy spuszcza, ogon podtuliwszy, zmyka;
Psiarnia z tryumfującym rzuca się hałasem
I skubie go po kudłach; zwierz zwraca się czasem,
Spojrzy, klapnie paszczęką i białych kłów zgrzytem
Ledwie pogrozi; psiarnia pierzcha ze skowytem:
Tak i Gerwazy z groźną cofał się postawą,
Wstrzymując napastników oczyma i ławą,
Aż razem z Hrabią wpadli w głąb ciemnej framugi. 
«Łapaj!» krzykniono znowu. Tryumf był nie długi:
Bo nad głowami tłumu Klucznik niespodzianie
Ukazał się na chórze, przy starym organie,
I z trzaskiem jął wyrywać ołowiane rury.
Wielką by klęskę zadał, uderzając z góry:
Ale już goście tłumnie wychodzili z sieni;
Nie śmieli kroku dostać słudzy potrwożeni
I chwytając naczynia w ślad panów uciekli,
Nawet nakrycia z częścią sprzętów się wyrzekli.
Któż ostatni, nie dbając na groźby i razy,
Ustąpił z placu bitwy? Brzechalski Protazy.
On, za krzesłem Sędziego stojąc niewzruszenie,
Ciągnął woźnieńskim głosem swoje oświadczenie,
Aż skończył i z pustego zszedł pobojowiska,
Kędy zostały trupy, ranni i zwaliska.
W ludziach straty nie było. Ale wszystkie ławy
Miały zwichnione nogi; stół także kulawy,
Obnażony z obrusa, poległ na talerzach
Zlanych winem, jak rycerz na krwawych puklerzach,
Między licznymi kurcząt i jendyków ciały,
W których piersi widelce świeżo wbite tkwiały.
Po chwili w Horeszkowskim samotnym budynku
Wszystko do zwyczajnego wracało spoczynku.
Mrok zgęstniał; reszty pańskiej wspaniałej biesiady
Leżą, podobne uczcie nocnej, gdzie na Dziady
Zgromadzać się zaklęte mają nieboszczyki.
Już na poddaszu trzykroć krzyknęły puszczyki
Jak guślarze: zdają się witać wschód miesiąca,
Którego postać oknem spadła na stół drżąca,
Niby dusza czyscowa; z podziemu, przez dziury,
Wyskakiwały na kształt potępieńców szczury:
Gryzą, piją; czasami w kącie zapomniana,
Puknie na toast duchom butelka szampana. 
Ale na drugim piętrze, w izbie, którą zwano,
Choć była bez zwierciadeł, salą zwierciadlaną
Stał Hrabia na krużganku zwróconym ku bramie,
Chłodził się wiatrem, surdut wdział na jedno ramię,
Drugi rękaw i poły u szyi sfałdował
I pierś surdutem, jakby płaszczem udrapował.
Gerwazy chodził kroki wielkimi po sali;
Obadwa zamyśleni, do siebie gadali:
«Pistolety — rzekł Hrabia — lub gdy chcą pałasze».
«Zamek — rzekł Klucznik — i wieś, oboje to nasze».
«Stryja, synowca — wołał Hrabia — całe plemię
Wyzywaj!» «Zamek — wołał Klucznik — wieś i ziemie
Zabieraj pan». To mówiąc, zwrócił się do Hrabi:
«Jeśli pan chce mieć pokój, niech wszystko zagrabi.
Po co proces, mopanku! sprawa jak dzień czysta:
Zamek w ręku Horeszków był przez lat czterysta;
Część gruntów oderwano w czasie Targowicy,
I jak pan wie, oddano władaniu Soplicy.
Nie tylko tę część, wszystko zabrać im należy,
Za koszta procesowe, za karę grabieży.
Mówiłem panu zawsze: procesów zaniechać;
Mówiłem panu zawsze: najechać, zajechać!
Tak było po dawnemu: kto raz grunt posiądzie,
Ten dziedzic; wygraj w polu, a wygrasz i w sądzie.
Co się tycze dawniejszych z Soplicami sprzeczek:
Jest na to od procesu lepszy Scyzoryczek;
A jeśli Maciej w pomoc da mi swą Rózeczkę,
To my we dwóch, Sopliców tych porzniem na sieczkę».
«Brawo! — rzekł Hrabia — plan twój, gotycko-sarmacki
Podoba się mi lepiej niż spór adwokacki.
Wiesz co? na całej Litwie narobim hałasu
Wyprawą niesłychaną od dawnego czasu.
I sami się zabawim. Dwa lata tu siedzę,
Jakąż bitwę widziałem? z chłopami o miedzę!
Nasza wyprawa przecież krwi rozlanie wróży.
Odbyłem taką jedną w czasie mych podróży.
Gdym w Sycylii bawił u pewnego księcia,
Rozbójnicy porwali w górach jego zięcia,
I okupu od krewnych żądali zuchwale;
My, zebrawszy naprędce sługi i wasale,
Wpadliśmy; ja dwóch zbójców ręką mą zabiłem,
Pierwszy wleciałem w tabor, więźnia uwolniłem.
Ach, mój Gerwazy! jaki to był tryumfalny,
Jaki piękny nasz powrót, rycersko-feudalny!
Lud z kwiatami spotykał nas; córka książęcia,
Wdzięczna zbawcy, ze łzami padła w me objęcia.
Gdym przybył do Palermo, wiedziano z gazety,
Palcami wskazywały mię wszystkie kobiety;
Nawet wydrukowano o całym zdarzeniu
Romans, gdzie wymieniony jestem po imieniu.
Romans ma tytuł: Polak, czyli tajemnice 
"""

print(translator.translate(text_example, "eng"))

print(len(text_example))

splited_text = re.split(r'\s+', text_example)

print(len(splited_text))
