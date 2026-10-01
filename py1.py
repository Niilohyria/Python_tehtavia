#1. Tee ohjelma, joka kysyy käyttäjältä, onko hän yli 18-vuotias, ja jos käyttäjä on yli 18-vuotias, kysyy häneltä, haluaako hän mennä sisään.
Ikä = int(input("Anna ikäsi"))
if Ikä >= 18:
    print ("Haluatko mennä sisään?")
else:
    print ("Et ole vielä täysi-ikäinen!")