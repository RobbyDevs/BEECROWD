import sys

input = sys.stdin.readline

while True:
        n = input()
        if n == '':
            break
        
        n = int(n)
        r = 1
        c = 1
        if n == 1:
            print(1)
            continue
            
        while r % n != 0:
            r = ((r *10) +1) % n
            c+=1
        
        print(c)



