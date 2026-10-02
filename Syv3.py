from datetime import datetime


syntymapäivämäärä_str = input("Syötä syntymäaikasi (muodossa pp/kk/vvvv): ")


syntymäaika = datetime.strptime(syntymapäivämäärä_str, "%d/%m/%Y")


nykyinen_päivämäärä = datetime.now()


ikä = nykyinen_päivämäärä.year - syntymäaika.year


if nykyinen_päivämäärä.month < syntymäaika.month or (nykyinen_päivämäärä.month == syntymäaika.month and nykyinen_päivämäärä.day < syntymäaika.day):
    ikä -= 1  


if ikä >= 18:
    print("Olet täysi-ikäinen.")
else:
 print("Et ole täysi-ikäinen.")