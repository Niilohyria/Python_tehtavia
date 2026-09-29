Lista = []
while True:
    Nimet = input("Anna etunimiä")
    Lista.append(Nimet)
    if Nimet == "":
        break
for i in Lista:
    print(i)