n = int(input())

v = [1, 3, 5, 10, 25, 50, 100]

for i in v:
    if n <= i:
        print(f'Top {i}')
        break