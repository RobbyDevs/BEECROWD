caso = 0
while True:
    try:
        caso +=1
        n = int(input())
        if n == 0:break
        
        a = n//50
        b = (n%50)//10
        c = ((n%50)%10)//5
        d = ((n%50)%10)%5
        
        print('Teste',caso)
        print(a,b,c,d)
        print()
    except EOFError:
        break