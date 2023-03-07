import random

user=int(input("Adja meg hogy fej(1) vagy írás(2): "))

fej=1
iras=2

pc=random.randint(1,2)
user=random.randint(1,2)

if(pc>user):
    print("A játékos vesztett")
else:
    print("A játékos nyert")



