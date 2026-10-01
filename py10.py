#10. Tee ohjelma, joka tarkistaa merkkijonosta, onko sen ensimmäinen kirjain sama kuin sen viimeinen kirjain.
Sana = input("Anna sana:")
if Sana[0] == Sana[-1]:
    print (f"Ensimmäinen ja  viimeinen kirjain on {Sana[0]}")
else:
    print ("Ensimmäinen ja viimeinen kirjain eroavat")