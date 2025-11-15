from math import comb
vf = 'AEIOUaeiou'
for w in range(int(input())):
    v = input()
    c = 1
    
    for i in v:
        if i not in vf:
            c *=2
        else:
            c*= 3
    
    
    
    print(c)
    