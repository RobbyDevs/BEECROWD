import sys
from math import pi

sys.stdin.readline

def volume(b,B,h): 
    return (1/3)*(pi*h)*((B**2)+(b**2)+(B*b))

def solve():
    n,l = map(int,input().split())
    
    b,B,h = map(int,input().split())
    e = 0
    d = h
    
    
    pCada = l/n 
    vol = volume(b,B,d) 
    
    flag= 0
    ant = 0
    
    while abs(vol-pCada) > 0.000001:
        flag+=1
        #if flag == 50: break
        
        #print(vol,"|",pCada)
        
        if vol > pCada:
            ant = d
            d = d/2
            
        elif vol < pCada:
            d = (d+ant)/2
            
        else:
            break
        vol = volume(b,B,d)
        
    print(f"{d:.2f}")
    

for w in range(int(input())):
    solve()
    

#190.58995431778078 | 200