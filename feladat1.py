penzosszeg = int(input("Mennyi összeget akar betenni: "))
arfolyam = int(input("Mennyi a árfolyam most: "))
ev = int(input("Mennyi évre szeretné betenni a pénzét: "))

osszeg = penzosszeg * (pow((1 + arfolyam / 100), ev))
FT = osszeg - penzosszeg
print("A kamatos kamatja", FT) 



