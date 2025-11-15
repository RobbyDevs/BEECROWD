import sys

n = sys.stdin.readline().strip()
m = int(sys.stdin.readline())

r = 0
for d in n:
    r = (r * 10 + ord(d) - 48) % m

print(r)
