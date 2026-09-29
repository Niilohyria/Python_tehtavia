from datetime import datetime
def Kello2(Aika):
    Aika2 = datetime.now().hour
    if Aika2 == Aika:
        print("Tämä aika on oikein")
    else:
        print("Nyt ei ole tämä aika")
Kello2(8)