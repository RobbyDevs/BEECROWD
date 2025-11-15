v = []
while True:
    try:
        t =input()
        
        v.append(int(input()))
        
    except EOFError:
        print(f'{(sum(v)/len(v)):.1f}')
        break