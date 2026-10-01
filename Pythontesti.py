def tarkista_taysi_ikaisuus(syntymavuosi):
    nykyinen_vuosi = 2024  # Päivitä tämä ajankohtaiseen vuoteen
    ika = nykyinen_vuosi - syntymavuosi
    if ika >= 18:
        return True
    else:
        return False

# Kysytään käyttäjältä syntymävuosi
syntyma_vuosi = int(input("Anna syntymävuotesi: "))
if tarkista_taysi_ikaisuus(syntyma_vuosi):
    print("Olet täysi-ikäinen.")
else:
    print("Et ole täysi-ikäinen.")
