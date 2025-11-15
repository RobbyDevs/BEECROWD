v = float(input())

if v <= 2000:
    print("Isento")

elif v >2000 and v <= 3000:
    print(f"R$ {((v-2000)*0.08):.2f}")


elif v>3000 and v <= 4500:
    print(f"R$ {(((v-3000)*0.18)+(1000*0.08)):.2f}")

else:
    print(f"R$ {(((v-4500)*0.28)+(1000*0.08)+(1500*0.18)):.2f}")