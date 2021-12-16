print("Program zjisti zda dane slovo obsahuje samohlasky")
slovo = input("Zadej slovo: ")
samohlasky = False
for znak in slovo:
    if znak in "aáeéěiíoóuúůyý":
        samohlasky = True
        break
if samohlasky:
    print(slovo, "Obsahuje samohlasky")
else:
    print(slovo, "Neobsahuje samohlasky")
    
    
    
print("Program zjistí z čeho se skládá slovo.")
slovo = input("Zadejte slovo: ")
samohlasky = 0
souhlasky = 0
ostatni = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúůyý":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisel = cisel + 1
    else:
        ostatni = ostatni + 1
print(slovo, "má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisel)
print("ostatních znaků...", ostatni)
input("\nAplikaci ukončíte stisknutím libovolné klávesy...")



print("Dotěrná aplikace")
pokracovat = True
while pokracovat:
    slovo = input("\nNapište Python pro ukončení: ")
    if (slovo == "Python" or slovo == "python"):
        print("\nSlovo zadáno!")
        pokracovat = False
    else:
        pass # nic se nestane
input("\nAplikaci ukončíte stisknutím libovolné klávesy...")


print("Kalkulačka\n")
pokracovat = True
while pokracovat:
    prvni_cislo = int(input("Zadejte první číslo: "))
    druhe_cislo = int(input("Zadejte druhé číslo: "))
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("5 - umocňování")
    cislo_operace = int(input("Zadejte číslo operace: "))
    if cislo_operace == 1:
        print("Jejich součet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Jejich rozdíl je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Jejich součin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        print("Jejich podíl je:", prvni_cislo / druhe_cislo)
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná volba!")
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si zadat další příklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            nezadano = False
        elif (odpoved == "n" or odpoved == "N"):
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nStiskněte libovolnou klávesu...")
