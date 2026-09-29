lista = []
while True:
    nimi = input("Anna etunimi:")
    if nimi == "":
        break
    lista.append(nimi)
print(f"Nimet listassa{lista}")