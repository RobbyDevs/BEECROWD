for w in range(int(input())):
    
    va,vb = map(str,input().split())
    vc = []
    m = min(len(va),len(vb))
    for i in range(m):
        vc.append(va[i])
        vc.append(vb[i])
        
    if len(va) > len(vb):
        print(f"{''.join(vc)}{va[(len(vb)):]}")
    elif len(vb) > len(va):
        print(f"{''.join(vc)}{vb[(len(va)):]}")
    else:
        print(''.join(vc))