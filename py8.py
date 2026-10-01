#8. Tee ohjelma, joka kysyy käyttäjältä uutta lukua, kunnes käyttäjän luku on sama kuin edellinen luku.
Luku1= input("Anna luku:")
while True:
    Luku2= input("Toista luku:")
    if Luku1 == Luku2:
     break
    else:
        print ("Ei ollut sama!")

print ("Oli sama!")