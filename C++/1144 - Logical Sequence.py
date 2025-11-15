n = int(input())

a = 0
b = 1
c = 1

x = 0
y = 0
j = 1

for i in range(1,(n*2)+1):
    if i%2 !=0:
        a +=1
        b +=x
        x +=2
        c +=y
        y += j*6      
        
    else:
        b+=1
        c+=1
        j+=1
        
    
    print(a,b,c)

