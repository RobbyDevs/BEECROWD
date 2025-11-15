A,B,C = map(float,input().split())

R1 = 0
R2 = 0

delta = B**2-4*A*C

if delta < 0 or A == 0:
    print("Impossivel calcular")

else:
    R1 = (-B + (delta ** (1 / 2)))/ (2*A)
    R2 = (-B - (delta ** (1 / 2))) / (2*A)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")