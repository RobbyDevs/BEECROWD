while True:
    hi,mi,hf,mf = map(int,input().split())
    c = 0
    if hi+mi+hf+mf == 0:
        break
    ti = (hi*60) + mi
    tf = (hf*60) + mf
    
    #print(ti,tf,end=" >> ")
    
    if tf > ti:
        print(tf-ti)
        
    elif tf < ti:
        print(abs(ti-tf-1440))
        
    else:
        print(1440)


    
#1440