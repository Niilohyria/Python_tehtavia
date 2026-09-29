sukunimet = [

"Vanni",

"Visanti",

"Rantasalo",

"Wuorimaa",

"Kilpi",

"Jalas",

"Kaira",

"Poijärvi",

"Linnala",

"Koskenniemi",

"Arni",

"Hainari",

"Pohjanpalo",

"Jännes",

"Kuusi",

"Talas",

"Rautapää",

"Aura",

"Wiherheimo",

"Kuusisto",

"Rantakari",

"Pinomaa",

"Paasilinna",

"Pihkala",

"Halsti",

"Kallia",

"Haarla",

"Harva",

"Heikinheimo",

"Päivänsalo",

"Helanen",

"Hattara",

"Helismaa"]
kerro = input("Millä alkukirjaimella etsitään:")
for i in range (len(sukunimet)):
    if sukunimet [i].startswith(kerro):
        print(sukunimet[i])