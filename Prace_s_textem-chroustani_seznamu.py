
# 5 Seznamy čísel
# pohodička
# Mějme zadaný následující seznam

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
# Vytvořte seznam, který obsahuje

# každé z čísel ze seznamu cisla vynásobené dvěma,
# každé z čísel ze seznamu cisla s opačným znaménkem,
# každé z čísel ze seznamu cisla umocněné na druhou,
# každé z čísel ze seznamu cisla jako řetězec.

a = [cislo*2 for cislo in cisla]
b = [cislo*(-1) for cislo in cisla]
c = [cislo**2 for cislo in cisla]
d = [str(cislo) for cislo in cisla]


# 6 Seznamy řetězců
# Mějme zadaný následující seznam

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
# Vytvořte seznam, který obsahuje

# počty písmen ve všech jménech,
# všechna jména napsaná velkými písmeny,
# všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
# všechna jména převedená na malá písmena s koncovkou '@email.cz'.

a = [len(jmeno) for jmeno in jmena]
b = [jmeno.upper() for jmeno in jmena]
c = [jmeno + 'a' for jmeno in jmena]
d = [jmeno.lower() + 'email.cz' for jmeno in jmena]



# 7 Seznam teplot
# Mějme zadaný následující seznam naměřených teplot.
# Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech
# - ráno, v poledne, večer a v noci.

teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]

# Vytvořte seznam průměrných teplot pro každý den.
# Vytvořte seznam ranních teplot.
# Vytvořte seznam nočních teplot.
# Vytvořte seznam dvouprvkových seznamů obsahujících pouze denní a noční teplotu.
# Spočítejte celkovou průměrnou teplotu za celý týden.

a = [sum(day)/len(day) for day in teploty]
b = [day[0] for day in teploty]
c = [day[-1] for day in teploty]
d = [[day[0], day[1]] for day in teploty]

# Vice moznych reseni
all_temperatures = [teplota for den in teploty for teplota in den]
total_avg = sum(all_temperatures)/len(all_temperatures)

# 8 Čtení kódu
# Popište vlastními slovy co následující výrazy udělají se zadaným seznamem seznam. Až když máte ve svojí hlavjénce jasno, tak je zkuste napsat do Python konzole a ověřte, zda jste měli pravdu.

seznam = [1, 4, 9, 16, 25, 36, 49, 64]
[x**0.5 for x in seznam]
[x % 2 for x in seznam]
[[x // 2, x % 2] for x in seznam]

seznam = ['12.03.2014', '10.01.2015', '06.06.1986']
[int(datum[3:5]) for datum in seznam]
[int(datum[:2])-1 for datum in seznam]
[
[int(datum[:2]), int(datum[3:5]), int(datum[6:])] for datum in seznam
]
[datum.split('.') for datum in seznam]
['/'.join(datum.split('.')) for datum in seznam]
