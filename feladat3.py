Lszam = []

szam=input("szám: ")

while(szam!=""):
    Lszam.append(int(szam))
    szam=input("Ha akar írjon be még egy számot: ")

print(sum(Lszam))