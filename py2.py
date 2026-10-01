#2. Tee ohjelma, joka tarkistaa, onko käyttäjän antama luku jaettava kolmella, ja jos se on, lisää siihen yksi ja printtaa se.
Luku = int(input("Anna luku"))
if Luku % 3 == 0:
    print(Luku + 1)
else:
    print ("Lukusi ei ole jaettavissa kolmella")