for w in range(int(input())):
    
    
    
    a1 = a2 = 0
    con = 0
    for i in input():
        if a1>0 and i!='a':
            con = 1
        if con ==0:
            
            if i == 'a':
                a1 +=1
        else:
            if i == 'a':
                a2 +=1
        
    
    
    r = 'a'*(a1*a2)
    print(f'k{r}')