import sys

input = sys.stdin.readline
def solve():
    a = len(input())-1
    b = len(input())-1
    
    if b>a:
        print("no")
    else:
        print("go")
    
solve()
    