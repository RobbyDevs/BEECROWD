import sys 
input = sys.stdin.readline

def primo(valor):
    if valor <=1:
        return 0
    elif valor <=3:
        return 1
    elif valor %2 == 0  or valor%3 == 0:
        return 0 
    
    else:
        p = 5
        
        while p*p <= valor:
            if valor%p == 0 or valor % (p+2) == 0:
                return 0
            p+=6
        return 1

def solve(n):
    v = []
    for w in range(n):
        v.append(int(input()))
        
    k = int(input())
    ans = 0
    for i in range(n-1,-1,-k):
        ans+=v[i]
    if primo(ans):
        print("You?re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
        print("Bad boy! I?ll hit you.")
    
            


while True:
    linha = input()
    if linha == '':
        break
    
    solve(int(linha))
    
    
