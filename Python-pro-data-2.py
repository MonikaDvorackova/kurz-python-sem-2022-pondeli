
# 1 Přidej k regulárnímu výrazu na číslo účtu možnost předčíslí
# Pokud bychom neuvažovali předčíslí, stačí nám regulární výraz, který by měl pasovat např. na číslo účtu 2300117015/2010. Nesmíme zapomenout na zpětné lomítko před lomítkem., tj. na začátku může být 0 až 6 čísel a za nimi může (ale nemusí) být pomlčka. Předčíslí 

# \d{0,6}-?\d{6,10}/\d{4}

# 2 Nejmenovaná česká banka rozlišuje typy účtů podle číslic na začátku čísla. Například je-li první číslice 1, jedná se o investiční účet, je-li první číslice 2, jde o bankovní účet. Uvažujme, že naše tajemná banka má kód (poslední čtyři čísla) 2100. # Uprav regulární výraz (nemusíš řešit předčíslí) tak, aby na prvním místě mohla být pouze 1 nebo 2.

# Uvažuj, že na druhém místě mohou být jen číslice 0, 1 nebo 2.

# Číslo účtu podruhé
# [12][1-3]\d{6,8}/2100

# 3 Standardní registrační značky automobilů, vydané od roku 2004, mají následující formát:
# Na prvním místě je číslo.
# Na druhém místě písmeno, které označuje kraj.
# Na třetím místě je číslo nebo písmeno.
# Na čtvrtém místě je mezera a následuje čtveřice čísel.
# Ověřit si ho můžeš na následujících značkách, které mají správný formát
# 4A6 8244
# 6B2 6635
# 2AD 3824
# 7C1 5025
# Napiš regulární výraz, který bude kontrolovat formát registrační značky. Ověřit si ho můžeš na následujících značkách, které mají špatný formát.
# AC8 5484
# 924 1541
# 8A2 25C2
# 3P 4564
# 1A 25364

# Registrační značka
# \d[A-Z]\w \d{4}
# \d(A|B|C|E|H|J|K|L|M|P|S|T|U|Z)\w \d{4}

# 4 V Česku máme standardně devítimístná telefonní čísla. Napiš regulární výraz, který sedí na “naše” telefonní čísla.

# Často se telefonní číslo rozděluje na trojice, které jsou odděleny mezerou. Uprav svůj výraz tak, aby odpovídal číslům s mezerou i bez mezery.

# Před telefonní číslo je výhodné přidat mezinárodní předvolbu (v našem případě +420), aby nám mohli volat i lidé ze zahraničí. Přidej to ke svému regulárnímu výrazu.
# +420 776 636 890
# 665676234

#Telefonní číslo
#(\+420)? ?\d{3} ?\d{3} ?\d{3}

# 5 Napiš regulární výraz, který z následujícího řádku vybere celé názvy ministerstev. 

# Ministerstvo pro místní rozvoj, Celní správa České republiky, Ministerstvo životního prostředí, Ministerstvo práce a sociálních věcí, Český statistický úřad, Nejvyšší kontrolní úřad

# Ministerstvo[\w ]*

# 6 Uvažuj vyhlášku, která definuje maximální hmotnosti vozidel u trojnápravy nákladních vozidel a jejíž zjednodušený text je níže. Napiš 2 regulární výraz. Prvním zjistíš limit (nebo limity) vzdáleností náprav v metrech a druhým maximální povolenou hmotnost v tunách.
# Maximální hmotnosti trojnápravy při dílčím rozvoru náprav jsou:
# do 1,3 m včetně - 21,00 t,
# nad 1,3 m do 1,4 m včetně - 24,00 t,
# nad 1,4 m do 1,8 m včetně - 27,00 t,

# \d{1}\,\d{1} m
# \d{2}\,\d{2} t

# 7 Spisová značka, tj. označení spisu u soudu, má zpravidla následující formát:
# číslo soudního oddělení (např. 1 až 2 čísla),
# rejstříková značka (např. jedno až tři velká písmena),
# běžné číslo, podle toho kdy k soudu věc přišla (např. 1 až 4 čísla),
# lomítko a za ním ročník (4 čísla).
# Může vypadat například takto: 63 C 397/2014. Napiš regulární výraz a na tomto příkladu jej vyzkoušej.

# \d{2} [A-Z] \d{1,4}/\d{4}

# 8 Římské číslice se dodnes používají například pro označení století, pořadí panovníků a papežů atd. Zkus sestavit regulární výraz, který zachytí římské číslice obsahující znaky I, V a X.

# IX. století
# Matematika pro VII. třídu
# Game of Thrones III
# Karel IV.
# papež Benedict V.
# Bělá je X. část statutárního města Děčín.
# III. patro
# II. stupeň povodňové aktivity
# (V|X|I)+
# I?(V|X)?I{0,3}

import re 

# 9 Náš systém vyžaduje od uživatele zadání uživatelského jména. Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé. Požádej uživatele o zadání uživatelského jména a pomocí regulárního výrazu vyhodnoť, zda je zadané správné.

import re
regularni_vyraz = re.compile(r"[a-z]{1,8}")
uzivatelske_jmeno = input("Zadej uživatelského jména: ")
vysledek = regularni_vyraz.fullmatch(uzivatelske_jmeno)
if vysledek:
    print("Uživatelské jméno je v pořádku.")
else:
    print("Uživatelské jméno nesplňuje požadavky")

# 10 Uprav program na ověření e-mailu tak, aby akceptoval i e-maily, které mají v první části tečku, např jiri.pesik@python.cz.

import re
regularni_vyraz = re.compile(r"\w+\.\w+@\w+\.cz")
email = "jiri.pesik@python.cz"
vysledek = regularni_vyraz.fullmatch(email)
if vysledek:
    print("E-mail jméno je v pořádku.")

# 11 Uvažujme aplikaci, která si ukládá informace o činnosti uživatelů do textového souboru. Příklad souboru je níže.

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""

# Napiš program, který vypíše všechna telefonní čísla, která jsou v textovém souboru zmíněna.
# Nahraď tato telefonní čísla nějakým řetězcem (např. “XXX”), aby nebyla v záznamech dostupná.

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""
import re
regularniVyraz = re.compile(r"[+\d]{13}")
vysledky = regularniVyraz.findall(zaznamy)
for vysledek in vysledky:
    print(vysledek)
anonymni_zaznamy = regularniVyraz.sub("X" * 9, zaznamy)
print(anonymni_zaznamy)

# 12 Adresy webových stránek zpravidla začínají záhadným shlukem písmen http:// nebo https://. Například náš web najdete pod adresou https://kodim.cz. Zkrátka HTTP nebo HTTPS je ve skutečnosti označení protokolu, což je nějaký popis toho, jak by měla vypadat komunikace mezi dvěma zařízeními. Standardního tvaru můžeme využít, abychom z textu vytáhli všechny adresy. Napiš program, který z proměnné emailSRadami vytáhne všechny webové stránky, které jsou tam zmíněny.

emailSRadami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz.
"""
email_s_radami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz a přihlašuj se na naše kurzy!
"""
import re
regularni_vyraz = re.compile(r"https?://[\w\.]*")
vysledky = regularni_vyraz.findall(email_s_radami)
for vysledek in vysledky:
    print(vysledek)

