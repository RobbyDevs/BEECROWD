import sys
input = sys.stdin.readline
global v

def solve(n):
    global v
    
    pilhas = []
    
    for i in range(n):
        if len(pilhas) == 0:
            pilhas.append(v[i])
        else:
            e = 0
            d = len(pilhas)
            
            
            while e < d:
                m = (e+d) // 2
                
                if pilhas[m] < v[i]:
                    e = m+1
                else:
                    d = m
                    
            if e == len(pilhas):
                pilhas.append(v[i])
            else:
                pilhas[e] = v[i]
                
    print(len(pilhas))


"""

3 4 9 11

"""
    

while True:
    n = input()
    
    if n == "" or n == "\n":
        break
    
    else:
        n = int(n)
        
        
        v = list(map(int,input().split()))
        
        
        while len(v) < n:
            v.extend(list(map(int,input().split())))
        
        #print(v)
        solve(n)