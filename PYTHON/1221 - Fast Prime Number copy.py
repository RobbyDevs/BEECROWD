def primo(n):
    if n <=1:
        return 0
    elif n<=3:
        return 1
    elif n%2 == 0 or n%3 == 0:
        return 0
    else:
        p = 5
        
        while p*p<=n:
            if n%p ==0 or n%(p+2)==0:
                return 0
        
            p+=6
        return 1

import sys
input = sys.stdin.readline

for w in range(int(input())):
    if primo(int(input())):
        print('Prime')
    else:
        print('Not Prime')
