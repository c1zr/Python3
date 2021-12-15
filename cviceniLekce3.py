jmeno = input("Zadej jmeno: ")
if (len(jmeno) >=3 and len(jmeno)<= 10):
    print("Normalni jmeno")
elif (len(jmeno) < 3):
    print("Kratke jmeno")
else:
    print("Dlouhe jmeno")
    
smajlik = input("zadej smajlika")
if(smajlik == ":-)"):
    print("Vesely smajlik")
elif(smajlik == ":-("):
    print("Smutny smajlik")
elif(smajlik == ":-*"):
    print("Pusovaci smajlik")
elif(smajlik == ":-P"):
    print("Vyplazovaci smajlik")
else:
    print("Zadany smajlik nesouhlasi s zadnym z uvedenych!")


a = float(input("Zadej hodnotu A"))
b = float(input("Zadej hodnotu B"))
c = float(input("Zadej hodnotu C"))

D = b ** 2 -4 * a * c
if (D > 0):
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("Rovnice ma dva koreny: ", x1, " a ", x2)
elif (D == 0):
    x = -b / (2 * a)
    print("Rovnice ma dvojnasobny koren: ",x)
else:
    print("Nema reseni, mozna")