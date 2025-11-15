import sys

input = sys.stdin.readline

dic = {}
cont = 0

def fib(x):
    if x in dic:
        return dic[x]
    
    if x == 0:
        dic[x] = [0,1]
        return dic[x]
    elif x == 1:
        dic[x] = [1,1]
        return dic[x]
    
    val1, cont1 = fib(x-1)
    val2, cont2 = fib(x-2)
    val = val1+val2
    cont  =  1+ cont1+cont2
    dic[x] = [val,cont]
    return dic[x]
    
for w in range(int(input())):
    x = int(input())
    fi = fib(x)
    #print(fi)
    #print(dic)
    print(f"fib({x}) = {fi[1]-1} calls = {fi[0]}")
    