tascii = {chr(i): i for i in range(29, 129)}
a = 0
while True:
    try:
        t = input()
        if not t:
            continue
        if a > 0:
            print()
        a+=1

        v = []
        counts = {}

        for char in t:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        for char, count in counts.items():
            v.append([count, tascii[char]])

        v.sort(key=lambda x: (x[0], -x[1])) 

        for count, ascii_value in v:
            print(f"{ascii_value} {count}")
    except EOFError:
        break