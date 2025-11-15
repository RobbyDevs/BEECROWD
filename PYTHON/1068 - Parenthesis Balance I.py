while True:
    
    try:
        
        v = [str(x) for x in input() if str(x) == '(' or str(x) == ')']
        s = []
        c = True
        for i in range(len(v)):
            if v[i] == '(':
                s.append(v[i])
            
            else:
                if len(s)>0:
                    s.pop()
                else:
                    c = False
                    break
        
        if c == True and len(s) == 0:
            print('correct')
        else:
            print('incorrect')
            
        
    except EOFError:
        break
    

    # (()))))
    # 
    