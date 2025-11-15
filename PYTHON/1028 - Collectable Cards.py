from math import gcd
for w in range(int(input())):
    
    a,b = map(int,input().split())
    
    while b != 0:
        a,b = b, a%b
    print(a)