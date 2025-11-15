from fractions import Fraction
for w in range(int(input())):
    
    n1,o1,d1,og,n2,o2,d2 = input().split()
    
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    
    nf = 0
    df = 0
    
    if(og == "+"):
        nf = (n1*d2)+(n2*d1)
        df = (d1*d2)
        

    elif(og == "-"):
        nf = (n1*d2)-(n2*d1)
        df = (d1*d2)
        
    elif(og == "/"):
        nf = n1*d2
        df = n2*d1

    else:
        nf = n1*n2
        df = d1*d2
    
    r = Fraction(nf,df)
    if nf%df == 0:
        
        print(f'{nf}/{df} = {r}/1')
    else:
        
        print(f'{nf}/{df} = {r}')
        