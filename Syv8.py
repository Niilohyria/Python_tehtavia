Asteikko = input("Käytetäänkö asteikkoa Celsius vai Fahrenheit?")
Lampotila = float(input("Anna lämpötila: "))

if Asteikko == "Fahrenheit":
    Nolla = 32
elif Asteikko == "Celsius":
    Nolla = 0
else:
    print("Älä pelleile")

if Lampotila < Nolla:
    print("Lämpötila on pakkasen puolella.")
elif Lampotila == Nolla:
    print("Lämpötila on nolla.")
else:
    print("Lämpötila on plussan puolella.")
