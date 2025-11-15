while True:
    l,c = map(int,input().split())
    if c == 0 and l == 0:
        break

    else:
        matriza = []
        for i in range(0,l):
            matriza.append(input())

        nl,nc = map(int,input().split())

        for i in range(0,c):
            for z in range(0,(nl//l)):
                for j in range(0,len(matriza[i])):
                    print(matriza[i][j]*(nc//c),end="")
                print(end="\n")
        print()