g1 = input()
g2 = input()
g3 = input()

if g1 == "vertebrado":
    if g2 == "ave":
        if g3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    
    else:
        if g3 =="onivoro":
            print("homem")
        else:
            print("vaca")

else:
    if g2 == "inseto":
        if g3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if g3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")