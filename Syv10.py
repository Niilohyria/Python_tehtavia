def Funktio():
    Etunimi = input("Anna etunimesi: ")
    return Etunimi

def Funktio2():
    Sukunimi = input("Anna sukunimesi: ")
    return Sukunimi

def Funktio3():
    Ikä = input("Anna ikäsi: ")
    return Ikä

def Funktio4():
    Kotikaupunki = input("Anna kotikaupunkisi: ")
    return Kotikaupunki

etunimi = Funktio()
sukunimi = Funktio2()
ikä = Funktio3()
kotikaupunki = Funktio4()
print(f"Hei {etunimi} {sukunimi}, olet {ikä} vuotta vanha ja kotikaupunkisi on {kotikaupunki}.")
