import sys

input = sys.stdin.readline

def isp(n):
    if n <=1:
        return 0
    
    elif n<=3:
        return 1
    
    elif n % 2 == 0 or n%3 == 0:
        return 0

    else:
        p = 5
        while p*p<= n:
            if n%p == 0 or n% (p+2) == 0:
                return 0
            
            p +=6
        return 1



n = int(input())

v = []
if isp(n):
    v.append(n)
    
i = n+2

if n%2 == 0:
    i+=1
while len(v) < 10:
    if isp(i):
        v.append(i)
    i+=2

vel = sum(v)
print(vel,"km/h")

h = int( 60e6/vel)

d = int(h/24)
print(f"{h} h / {d} d")
