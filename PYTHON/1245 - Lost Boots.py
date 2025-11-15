while True:
    try:
        
        ve = [[] for x in range(31)]
        vd= [[] for x in range(31)]
        s = r = c =0
        
        for i in range(int(input())):
            s = input()
            if s[3] == "E":
                if len(vd[int(s[:2])-30]) == 0:
                    ve[int(s[:2])-30].append(int(s[:2])-30)
                else:
                    vd[int(s[:2])-30].pop()
                    c+=1
            else:
                if len(ve[int(s[:2])-30]) == 0:
                     vd[int(s[:2])-30].append(int(s[:2])-30)
                else:
                     ve[int(s[:2])-30].pop()
                     c+=1
            
            
        print(c)
            
            
    except EOFError:
        break