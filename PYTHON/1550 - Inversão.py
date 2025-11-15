for w in range(int(input())):
    a,b = input().split()
    
    j = len(b)
    ans = 1
    if len(a) == 1:
        ans-=1
    for i in range(len(a)):
        j-=1
        ai = int(a[i])
        bi = int(b[j])
        if abs(ai-bi) !=0:
            ans+= abs(ai-bi)
            
    print(ans)
    
