x = input()
y = input()

s = "N"
for i in range(0,10,2):
    if x[i]==y[i]:
        s = "N"
        break
    else:
        s = "Y"

print(s)