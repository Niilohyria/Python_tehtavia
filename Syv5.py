Sallusanna = input("Luo oma salainen sanasi: ")

if len(Sallusanna) < 8:
    print("Salasana on liian lyhyt")
elif len(Sallusanna) > 20:
    print("Salasana on liian pitkä")
else:
    print("Salasana on sopivan pituinen")
if not any(char.isdigit() for char in Sallusanna):
    print("Salasanassa ei ole numeroa. Lisää ainakin yksi numero.")
else:
    print("Salasanassa on numero.")
