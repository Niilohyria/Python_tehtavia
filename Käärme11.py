Raha = float(input("Paljonko sinulla on rahaa?"))
Pizza = float(input("Paljonko pizza maksaa?"))
Summa = Raha - Pizza
if Summa > 0:
    print ("Nauti pizzasta!")
    print(f"Rahaa jäi {Summa} euroa.")
else:
    print("Rahasi eivät riitä!")