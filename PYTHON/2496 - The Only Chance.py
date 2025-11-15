for w in range(int(input())):
    
    l = int(input())
    va = input()
    vs = sorted(va)
    
    ind = 0
    
    vb =[]
    for i in range(l):
        if va[i]!=vs[i]:
            vb.append(i)
            
    if(len(vb)>2):
        print("There aren't the chance.")
    else:
        if(abs(vb[0])-vb[1]>1):
            print("There aren't the chance.")
        else:
            print("There are the chance.")
            
