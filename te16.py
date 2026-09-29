Lista = []
while True:
    Nimet = input("Anna etunimiä")
    Lista.append(Nimet)
    if Nimet == "":
        break
Lista.sort() 
for i in Lista:
    print(i)