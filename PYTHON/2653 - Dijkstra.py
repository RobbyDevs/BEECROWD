v = []
while True:
    try:
        v.append(input())
    except EOFError:
        
        print(len(list(set(v))))
        break