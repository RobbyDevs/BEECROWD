import sys
from math import gcd
input = sys.stdin.readline

while True:
    
    s = input()
    if s == '':
        break
    
    a,b = map(int,s.split())
    
    if a == b:
        print(4)
    else:
        
        g = gcd(a,b)
        a = 2*a
        b = 2*b
        if g == 1:
            
            print(a+b)
        else:
            print((a+b)//g)
        