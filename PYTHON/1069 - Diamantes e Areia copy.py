for w in range(int(input())):
    
    v = input();
    va = [];
    c = 0
    
    for i in v:
        if i == '<':
            va.append(i);
            
        elif i == '>':
            if len(va)>0:
                va.pop();
                c+=1;
            else:
                break;
    
        
    print(c);