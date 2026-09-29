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
kakkoslista = []
for i in sukunimet:
    if i[2].lower() == 'n': 
        kakkoslista.append(i)
for j in kakkoslista:     
    print(j)