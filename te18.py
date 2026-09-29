Lista=["Riikonen","Suomalainen","Huhtamäki","Mäkelä","Tapani","Mäkinen"]
Kerro = input("Millä alkukirjaimella etsitään:")
Etsi = [Nimi for Nimi in Lista if Nimi.startswith(Kerro)]
print(Etsi)