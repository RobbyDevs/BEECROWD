import sys
input = sys.stdin.readline

while True:
    n = input()
    if n == '':
        break
    
    n = int(n)
    v = list(map(int,input().split()))
    va = [v[0]]
    ans = 0
    
    for i in range(1,n):

        if va[-1] < v[i]:
            va.append(v[i])
        else:
            while va:
                if va[-1] < v[i]:
                    break
                
                ans += va.pop()
            va.append(v[i])
            
    print(ans)