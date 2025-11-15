c,q = map(int,input().split())

cq,xs,xb,ts,r,t = 4.00,4.50,5.00,2.00,1.50,0.0

if(c==1):
    t=cq*q

elif(c==2):
    t=xs*q

elif(c==3):
    t=xb*q

elif(c==4):
    t=ts*q

elif(c==5):
    t=r*q

print(f"Total: R$ {t:.2f}")


