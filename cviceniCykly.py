pocet = int(input("Pocet ryb"))
i = 0
while(i < pocet):
    print("<° )))-<")
    i = i + 1
    

lahve = 10
while(lahve >= 1):
    if(lahve >= 5):
        print(lahve, " zelených lahví stojí na stole a jedna spadne")
    elif(lahve > 1):
        print(lahve, " zelené lahve stojí na stole a jedna spadne")
    else:
        print(lahve, " zelena lahev stojí na stole a jedna spadne")
    lahve = lahve -1
    
    
spodniMez = int(input("Zadej prvni cislo"))
horniMez = int(input("Zadej druhge cislo"))

for pozice in range(spodniMez, horniMez +1, 1):
    if pozice % 3 == 0:
        print(pozice, " ano")
    else:
        print(pozice, " ne")
    
    
    