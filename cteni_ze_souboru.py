
# 1 Výplata přesněji 
# Zatím jsme  výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. Vytvořte proto textový soubor vykaz.txt, který bude obsahovat 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.
# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. Vytiskněte tento seznam na konzoli funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

with open('vykaz.txt') as f:
    # Takto bych to napsala elegantne a zkracene, samozrejme je mozne si rozepsat kod do vice radku
    hours_per_month = [int(line) for line in f.readlines()]

hour_pay = int(input('Zadej hodinovou mzdu: '))

# Mohli bychom toto predelani na cislo klidne dat do try, except bloku
# try:
#     hodinova_mzda = int(input('Zadej hodinovou mzdu: '))
# except ValueError:
#     print('Zadej ciselnou hodnotu!')
#     exit(1)

year_salary = sum(hours_per_month) * hour_pay
average_per_month = round(year_salary / len(hours_per_month))

print(f'Celkovy rocni plat: {year_salary} Kc')
print(f'Prumerny mesicni plat: {average_per_month} Kc')

# Pokud byste chteli vyuzit funkce, muzete si klidne obalit kazde cviceni do funkce a tu potom pouze volat
def vyplata():
    with open('vykaz.txt') as f:
        hours_per_month = [int(line) for line in f.readlines()]

    hour_pay = int(input('Zadej hodinovou mzdu: '))
    year_salary = sum(hours_per_month) * hour_pay
    average_per_month = round(year_salary / len(hours_per_month))

    print(f'Celkovy rocni plat: {year_salary} Kc')
    print(f'Prumerny mesicni plat: {average_per_month} Kc')

# vyplata()


# 2 Počet slov
# Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě. Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.
# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu.
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem.
# Vypište na výstup seznam hodnot udávající počty slov na každém řádku.
# Vypište na výstup celkový počet všech slov v souboru.

def pocet_slov():
    with open('praha.txt') as f:
        lines = f.readlines()

    seznam_radku_slov = [line.split() for line in lines]
    print(seznam_radku_slov)
    pocet_slov_na_radkach = [len(line) for line in seznam_radku_slov]
    print(pocet_slov_na_radkach)
    celkovy_pocet_slov = sum(pocet_slov_na_radkach)
    print(celkovy_pocet_slov)

# pocet_slov()

# 3 Půjčovna
# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.
# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().
# Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.

def pujcovna():
    filename = input('Zadej jmeno souboru s daty: ')
    with open(filename) as f:
        lines = f.readlines()

    # neprehledny one-liner pro fajnsmekry
    kilometry = sum([float(line.split()[1].replace(',', '.')) for line in lines])
    print(kilometry)

    # Po jednotlivych krocich (kazdy list comprehension jde samozrejme nahradit za klasicky for cyklus)
    spz_km = [line.split() for line in lines]
    pouze_km = [sk[1] for sk in spz_km]
    nahrazene_carky = [km.replace(',', '.') for km in pouze_km]
    float_hodnoty = [float(km) for km in nahrazene_carky]
    celkem_km = sum(float_hodnoty)
    print(celkem_km)

pujcovna()

# ZAPIS

"""
Rozepsaná výplata
Modifikujte program pro počítání výplaty z předchozí sekce tak,
aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.
Nejprve tyto informace vypište na výstup pomocí funkce print().
Poté program upravte tak, aby vypsal tyto výsledky do souboru.
"""
# Zase muzeme klidne rovnou pouzit pro kazde cviceni samostatnou funkci
# Ja to pouzivam protoze pak nemusim vice kodu komentovat

def rozepsana_vyplata():
    #  Z predchoziho cviceni
    with open('vykaz.txt') as f:
        hours_per_month = [int(line) for line in f.readlines()]
    hour_pay = int(input('Zadej hodinovou mzdu: '))

    # novy kod - print
    for month_hours in hours_per_month:
        month_salary = month_hours * hour_pay
        print(f'{month_salary} Kc')

    # novy kod - do souboru (varianta s list comprehension)
    with open('vyplata_vystup.txt', mode='w', encoding='utf-8') as file:
        lines = [f'{month_hours * hour_pay} Kc\n' for month_hours in hours_per_month]
        file.writelines(lines)

# rozepsana_vyplata()

"""
Hody kostkou
Napište program, který vytvoří seznam deseti náhodných hodů dvanáctistěnnou kostkou.
Nejdříve tento seznam vytiskněte na konzoli pomocí funkce print().
Upravte váš program tak, aby náhodné hody kostkou vypsal do souboru s názvem hody.txt na jeden řádek oddělené čárkou a mezerou.
Upravte váš program tak, aby počet hodů dostal jako parametr na příkazové řádce. Zkuste použitím vašeho programu vyrobit 100, 1000 a 10 000 hodů.
"""
import random
import sys

def hody_kostkou(args):
    # funkce z modulu random
    pocet_hodu = int(args[1])
    hody = [random.randint(1,6) for i in range(pocet_hodu)]
    # pouze print
    print(hody)

    # do souboru pomoci oddeleni carkami

    # pomoci for cyklu
    with open('hody.txt', mode='w', encoding='utf-8') as f:
        for hod in hody:
            f.write(f'{hod}, ')
        # Tady vam zustane carka a mezera na konci, nize jsou dlasi varianty

    # pomoci metody join si vytvorit string
    with open('hody.txt', mode='w', encoding='utf-8') as f:
        hody_s_carkami = ", ".join([str(hod) for hod in hody])
        f.writelines(hody_s_carkami)

    # A nebo pomoci for cyklu vytvorit string k zapisu
    with open('hody.txt', mode='w', encoding='utf-8') as f:
        content = ''
        for hod in hody:
            content += f'{hod}, '
        # Pokud nechcete mit za poslednim cislem carku a mezeru muzete pouzit metodu rstrip()
        # content = content.rstrip(', ')
        f.writelines(content)

# hody_kostkou(sys.argv)

"""
Dny v měsíci
Napište  program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Oddělte v souboru název měsíce a počet dnů pomocí tabulátoru.
Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy měsíc a počet dní.
"""

def dny_v_mesici():
    pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        for den in pocty_dni:
            f.write(f'{den}\n')

    # S nazvy mesicu
    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        for den in pocty_dni:
            f.write(f'{den}\n')
    # Muzete si na nazvy mesice vytvorit take list, pripadne upravit predchozi list, nebo treba pouzit nazvy mesicu z modulu calendar

    # Vlastni mesice
    months = ['Leden', 'Unor', 'Brezen', 'Duben', 'Kveten', 'Cerven', 'Cervenec', 'Srpen', 'Zari', 'Rijen', 'Listopad', 'Prosinec']

    # Mesice z modulu calendar
    # je treba posunou index, protoze promenna z modulu ma na 0 nic, a az na 1 leden atd.
    # import calendar
    # months = list(calendar.month_name)[1:]

    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        f.write(f'Mesic\tPocet dnu\n') # Pro zahlavi

        # zip dela ze dvou listu list dvojic https://docs.python.org/3/library/functions.html#zip
        for month, days in zip(months, pocty_dni):
            f.write(f'{month}\t{days}\n')
            # Mozna lepsi nez tabulator je zarovnat mesice na deset znaku zleva pomoci formatovan iv f stringu (jen pro zajimavost)
            # f.write(f'{month:<10}{days}\n')

    # slo by resit i s range(12) a indexovat oba listy stejnym indexem
    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        for i in range(12):
            f.write(f'{months[i]}\t{pocty_dni[i]}\n')


dny_v_mesici()
