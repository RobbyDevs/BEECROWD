while True:
    l,c = map(int,input().split())
    if l==0 and c==0:
        break
    else:
        isclean = False
        m = []
        for i in range(0,l):
            t = input()
            m.append(list(t))

        while isclean == False:
            isclean = True
            for j in range(0,l):
                for k in range(0,c):
                    if m[j][k] == "T":

                        if k<c-1: #DIREITA OK
                            if m[j][k+1] == "A":
                                m[j][k+1]= "T"
                                isclean = False

                        if k>0: #ESQUERDA OK
                            if m[j][k-1] == "A":
                                m[j][k-1] = "T"
                                isclean = False
                        
                        if j > 0: #BAIXO OK
                            if m[j-1][k] == "A":
                                m[j-1][k] = "T"
                                isclean = False
                        
                        if j < l-1: #CIMA OK  
                            if m[j+1][k] == "A":
                                m[j+1][k] = "T"
                                isclean = False

        for z in range(0,l):
            print("".join(m[z]))
        print()

