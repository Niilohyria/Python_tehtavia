while True:
    while True:
        Pituus = float(input("Anna pituus: "))
        if Pituus > 0:
            break
        print("Anna pituus uudelleen")

    while True:
        Hinta = float(input("Anna hinta: "))
        if Hinta > 0:
            break
        print("Anna hinta uudelleen")

    break  

if Pituus > 60:
    print(f"Hinta on {Pituus * 1.25 * Hinta}")
else:
    print(f"Hinta on {Pituus * 1.50 * Hinta}")
