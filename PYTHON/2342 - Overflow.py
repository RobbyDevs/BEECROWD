n = int(input())

p,c,q = map(str,input().split())

p,q = int(p),int(q)

if (c == "+"):
    if p+q > n:
        print("OVERFLOW")
    else:
        print("OK")

elif c == "*":
    if p*q > n:
        print("OVERFLOW")
    else:
        print("OK")