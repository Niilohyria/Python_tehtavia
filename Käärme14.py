summa = 0  
while True:
    luku = int(input("Anna luku:"))  
    if luku == 0:  
        break
    summa += luku

print(f"Kaikkien syötettyjen lukujen summa on: {summa}") 
