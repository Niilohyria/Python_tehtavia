print("Syötä kokonaislukuja, 0 lopettaa:")
Lukuja = 0
Summa = 0
while True:
    Luku = int(input("luku: "))
    if Luku == 0:
        break
    Lukuja += 1
    Summa += Luku
if Lukuja > 0:
    print("Lukuja yhteensä", Lukuja)
if Lukuja > 0:
    print("Lukujen summa", Summa)
if Lukuja > 0:
    print("Lukujen keskiarvo", Summa/Lukuja)
