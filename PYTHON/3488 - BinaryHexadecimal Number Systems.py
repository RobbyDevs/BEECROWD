import sys
from math import log2
input = sys.stdin.readline

n = int(input())

if n<=0:
    print('false')
else:
    ans = log2(n)

    if ans - int(ans) == 0:
        print("true")
    else:
        print("false")
        

"""


"""