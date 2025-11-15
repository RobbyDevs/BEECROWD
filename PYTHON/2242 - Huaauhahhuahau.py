s = 'aeiou'

v = [str(x) for x in input() if x in s]


if v == list(reversed(v)):

    
    print('S')
else:
    print('N')