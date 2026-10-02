Niilo = input ("Hei, Niilo, kerro nimesi")
if Niilo == "Niilo":
    print("Mä tiesin et se oot sä, broidi")
else:
    print("Kuka hitto sä oot...")
Luku1 = int(input("Kerro luku tai saat turpaan"))
Luku2 = int(input("Kuulitko sä mua?"))
Summa = print (f"Tässä on summa {Luku1+Luku2}")
Ukul1 = int(input("Kerro pliis se luku, nyaa:-3"))
Ukul2 = int(input("Jookooo☆*: .｡. o(≧▽≦)o .｡.:*☆"))
Erotus = print (f"Tässä on erotus {Ukul1-Ukul2}")
Luvut1 = int(input("En jaksa enää pelleillä, saisinko vaan luvun?"))
Luvut2 = int(input("Danke schön, mein bruder."))
Tulo = print (f"Tässä on tulo {Luvut1*Luvut2}")
Numero1 = float(input("You know how it goes..."))
Numero2 = float(input("Thanks for making my life easier. It's really tough, i have a wife and 10 brats at home... *Starts rambling incoherently*"))
Osamäärä = print (f"Tässä on osamäärä {Numero1/Numero2}")
Tärkeäluku = int(input("Tis nambö is ekstriimli impoortant"))
if Tärkeäluku  > 0:
 print("Tämä on positiivinen luku")
elif Tärkeäluku < 0:
 print("Tämä on negatiivinen luku")
else:
 print("Tämä on nolla")
Nampöörs = [1,2,3,4,5,6,7,8,9,10]
Kirjankäsky = int (input("Kerro luku, joka on listassa"))
for x in Nampöörs:
 print(x)
Nimi = input ("Yksi nimi, kiitos")
Ikä = int(input ("Yksi ikä, kiitos"))
Kotikaupunki = input ("Yksi kotikaupunki, kiitos")
Kotimaa = input ("Yksi kotimaa, kiitos")
if Ikä  >= 18:
 print (f"Nimesi on {Nimi}. Olet täysi ikäinen. Kotikaupunkisi on {Kotikaupunki} ja kotimaasi on {Kotimaa}")
else:
   print (f"Nimesi on {Nimi}. Et ole täysi ikäinen. Kotikaupunkisi on {Kotikaupunki} ja kotimaasi on {Kotimaa}")
Number = int(input("Gimme dhose nambörs."))
Number2 = int(input("Seim hiör."))
print (f"Lukujen summa on {Number + Number2}, lukujen erotus on {Number - Number2}, lukujen tulo on {Number * Number2}, Lukujen osamäärä on {Number / Number2}")
A = int(input("Anna vielä luku"))
B = int(input("Anna vielä luku"))
C = int(input("Anna vielä luku"))
D = int(input("Anna vielä luku"))
E = int(input("Anna vielä luku"))
if A > B and A > C and A > D and A > E:
 print(f"Luku {A} on suurin")
elif B > A and B > C and B > D and B > E:
 print(f"Luku {B} on suurin")
elif C > A and C > B and C > D and C > E:
 print(f"Luku {C} on suurin")
elif D > A and D > B and D > C and D > E:
 print(f"Luku {D} on suurin")
elif E > A and E > B and E > C and E > D:
 print(f"Luku {E} on suurin")
if A < B and A < C and A < D and A < E:
 print(f"Luku {A} on pienin")
elif B < A and B < C and B < D and B < E:
 print(f"Luku {B} on pienin")
elif C < A and C < B and C < D and C < E:
 print(f"Luku {C} on pienin")
elif D < A and D < B and D < C and D < E:
 print(f"Luku {D} on pienin")
elif E < A and E < B and E < C and E < D:
 print (f"Luku {E} on pienin")
Sallusanna = input("Luo oma salainen sanasi")
if len(Sallusanna) < 8:
 print ("Salasana on liian lyhyt")
elif len(Sallusanna) > 20:
 print ("Salasana on liian pitkä")
else:
 print ("Salasana on sopivan pituinen")
Lukutoukka = int(input("Tarkistetaan onko sulla parillinen luku"))
if Lukutoukka %2 == 0:
 print ("Lukusi on parillinen")
else:
 print ("Lukusi ei ole parillinen")