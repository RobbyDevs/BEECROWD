s,t,f = map(int,input().split())
h=0

if s + t >= 24:
    h = -24 + ((s+t)+f) 

elif (s+f)<0:
    h = 24 + (t+s+f)

else:
    h = t+s + f


print(h)