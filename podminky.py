


cislo = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if(cislo > 0):
    print("Zadal jsi cislo vetsi nez nula, to znamena, ze muzeme odmocnit")
    odmocnina = cislo ** (1/2)
    print("Odmocnina z čísla", cislo, "je", odmocnina)
else:
    print("Odmocnina ze záporného čísla neexistuje!")
    print("Děkuji za zadání")
    


cislo = 0 # do čísla si přiřadíme na začátku 0
if (cislo == 0): # pokud je číslo 0, dáme do něj jedničku
    cislo = 1
else: # pokud je číslo 1, dáme do něj nulu
    cislo = 0

print(cislo)



cislo = int(input("Zadej cislo v rozmezi 10 az 20: "))
if ((cislo >= 10) and (cislo <=20)):
    print("Zadal jsi spravne")
else:
    print("Zadal jsi spatne")
    
