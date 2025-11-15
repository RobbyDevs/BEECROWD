lista = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen","Rudolph"]

val = list(map(int,input().split()))
print(lista[(sum(val)%9)-1])