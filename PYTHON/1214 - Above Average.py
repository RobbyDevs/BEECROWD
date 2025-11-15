for w in range(int(input())):
    
    v = list(map(int,input().split()))
    
    av = sum(v[1:])/v[0]
    c = 0
    for i in v[1:]:
        if i > av:
            c+=1
    print(f'{((c/v[0])*100):.3f}%')