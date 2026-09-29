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
    if i[-1].lower() == 's': 
        kakkoslista.append(i)
for j in kakkoslista:
    kakkoslista.sort()    
    print(j)