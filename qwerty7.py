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
kerro = input("Mitä kirjainta etsitään sukunimen 3:sta merkistä?")
for i in sukunimet:
    if i[2].lower() == kerro: 
     print(i)