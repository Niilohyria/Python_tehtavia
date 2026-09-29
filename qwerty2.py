lista = ["Pekkala","Suominen","Pitkämäki","Männikkö","Tapanila","Mäki"]
kerro = input("Millä alkukirjaimella etsitään:")
etsi = [nimi for nimi in lista if nimi.startswith(kerro)]
print(etsi)
