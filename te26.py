def lista(l):
    if l[0] > l[1] and l[0] < l[2] or l[0] < l[1] and l[0] > l[2]:
        print(l[0])
    if l[1] > l[0] and l[1] < l[2] or l[1] < l[1] and l[1] > l[2]:
        print(l[1])
    if l[2] > l[0] and l[2] < l[1] or l[2] < l[0] and l[2] > l[1]:
        print(l[2])
l = [0,9,4]
lista(l)
