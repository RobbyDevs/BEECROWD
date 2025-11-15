n = int(input())

for w in range(1,1000):
    
    
    if n != 0:
        
        p1 = input()
        p2 = input()

        print('Teste',w)
        for i in range(n):

            a,b = input().split()
            a = int(a)
            b = int(b)

            if (a+b)%2 == 0:
                print(p1)
            else:
                print(p2)
        print()
        n = int(input())
