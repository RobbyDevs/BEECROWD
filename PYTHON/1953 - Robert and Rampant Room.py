while True:
    try:
        
        n = int(input())
        if n == 0:break
        
        
        intru = 0
        EPR = EHD = 0
        for i in range(n):
            
            a,b = input().split()
            
            if b == 'EPR':
                EPR+=1
            elif b =='EHD':
                EHD +=1
                
            else:
                intru +=1
                
        print('EPR:',EPR)
        print('EHD:',EHD)
        print('INTRUSOS:',intru)
    except EOFError:
        break
    
