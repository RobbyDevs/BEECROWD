for w in range(int(input())):
    
    v = [str(x).lower() for x in input() if (ord(x)>64 and ord(x)) or (ord(x)>=96 and ord(x)<=121)]
    
    
    vf = [0 for x in range(26)]
    
    
    for i in v:
        vf[ord(i)-97]+=1

    
    vr = []
    maxif = 0
    
    for i in range(len(vf)):
        if vf[i]>maxif:
            maxif = vf[i]
            
    for i in range(len(vf)):
        if vf[i] == maxif:
            vr.append(chr(i+97))
            
    print(''.join(vr))
            