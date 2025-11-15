for w in range(int(input())):
    
    v = input()
    v1 = input()
    v2 = input()
    
    cv1 = 0
    cv2 = 0
    d1 = []
    d2 = []
    
    
    for i in range(len(v)):
        if v[i] == v1[i]:
            cv1 +=1
        else:
            d1.append(i)
            
        if v[i] == v2[i]:
            cv2 +=1
        else:
            d2.append(i)
            
            
    print('Instancia',w+1)
    
    if cv1>cv2:
        print('time 1')
        
    elif cv1<cv2:
        print('time 2')
    else:
        
        for i in range(len(d1)):
            if d1[i] > d2[i]:
                print('time 1')
                break
            elif d1[i] < d2[i]:
                print('time 2')  
                break
        else:
            print('empate')              
        
        
    print()