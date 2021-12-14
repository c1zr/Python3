pozdrav = input("ahoj, jak se jmenujes? ")
print(pozdrav)
jaky_jsi = input("Jaky jsi? ")
print(jaky_jsi)
print(pozdrav + " " + jaky_jsi )


zadej_cislo = int(input("Zadej cislo k umocnenni: "))
print("Vysledek je: ", zadej_cislo * zadej_cislo)



r = float(input("Zadej poloměr kruhu (cm): "))
o = 2 * 3.14 * r
s = 3.14 * r * r
print("Obvod zadaného kruhu je:", o, "cm")
print("Jeho obsah je", s, "cm^2")
input()