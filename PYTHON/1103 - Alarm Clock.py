while True:
    hi,mi,hf,mf = map(int,input().split())
    c = 0
    if hi+mi+hf+mf == 0:
        break
    
    
    m=h=0
    if mf >= mi:
        m = mf-mi
    else:
        m = 60-mi+mf
        c=1
    
    if hf > hi:
        h = hf-hi
    elif hf == hi:
        h +=23
    else:
        h += 24-hi + hf
    
    if hf == hi and mf == mi:
        h = 24
        m = 0
        
    r = (h*60)+m
    print('>>')
    print(h,m,r)
    #print(r)
    
