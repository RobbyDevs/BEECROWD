caso = 0
while True:
    caso+=1
    a,b = map(int,input().split())
    #v = []
    vf = [0]*(a+1)
    v = []

    if b == a and a == 0:
        break
    
    for i in range(b):
        x,y = map(int,input().split())
        vf[x-1] +=1
        vf [y-1] +=1

    mai = max(vf)

    for i in range(len(vf)):
        if vf[i] == mai:
            v.append(i+1)
    print('Teste',caso)
    #v.sort()


    print(*v,sep=' ',end=' \n')
    print()
    




