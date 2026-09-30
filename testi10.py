from collections import Counter  

Anagrammi1 = input("Anna merkkijono")
Anagrammi2 = input("Vielä kerran")

if len(Anagrammi1) != len(Anagrammi2):  
    print("Merkkijonot eivät ole anagrammeja")
else:
    if Counter(Anagrammi1) == Counter(Anagrammi2):  
        print("Merkkijonot ovat anagrammeja")
    else:
        print("Merkkijonot eivät ole anagrammeja")