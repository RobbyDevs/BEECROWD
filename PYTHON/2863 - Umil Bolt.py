while True:
    try:
        v = [float(input()) for x in range(int(input()))]
        
        print(min(v))
    except EOFError:
        break