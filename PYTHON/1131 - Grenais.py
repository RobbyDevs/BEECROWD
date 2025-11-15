j = 1
inte=grem=gr=g=em=ii=i=gi=0
while j != 2:
    gr +=1
    ii,gi = map(int,input().split())
    g += gi
    i += ii
    if(ii > gi):
        inte+=1
    elif(gi>ii):
        grem+=1
    else:
        em+=1
    j = int(input("Novo grenal (1-sim 2-nao)\n"))
print(f'{gr} grenais\nInter:{inte}\nGremio:{grem}\nEmpates:{em}')
if inte>grem:
    print("Inter venceu mais")
elif grem>inte:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")

