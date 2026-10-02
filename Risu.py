def viiva(leveys, merkkijono):
    if merkkijono == "":
        merkkijono = "*"
    print(leveys * merkkijono)
if __name__ == "__main__":
    viiva(5, "")
def risunelio(merkki):
    i=1
    a=2
    while i<=a:
        print(merkki)
        i+=1
     
    
if __name__ == "__main__":
    risunelio("##########")