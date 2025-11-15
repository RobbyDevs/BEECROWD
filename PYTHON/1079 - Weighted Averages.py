t = int(input())

for w in range(t):
    v = list(map(float,input().split()))
    
    m = ((v[0]*2)+(v[1]*3)+(v[2]*5))/10
    print(f'{m:.1f}')