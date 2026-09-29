Lista = []
Laskuri = 0  

while True:
    Luku = int(input("Anna lukuja yhdestä yhdeksään: "))
    if Luku > 9 or Luku < 0:
        print("Ei käy")
    elif Luku == 0:
        break
    else:
        Lista.append(Luku)
for i in Lista:
    print(i + Laskuri) 
    Laskuri += 1 
