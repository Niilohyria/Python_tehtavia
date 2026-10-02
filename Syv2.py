Luku = int(input("1-10"))
if (Luku < 1 or Luku > 10):
 print ("Tee nyt vähän paremmin...")
else:
    for i in range(1, 11):
        print(i)
        if i == Luku:
           break