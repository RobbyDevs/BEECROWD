n1,n2,n3,n4 = map(float,input().split())

m = ((n1*2)+(n2*3)+(n3*4)+n4)/10


print(f"Media: {m:.1f}")
if m >= 7:
    print("Aluno aprovado.")

elif m < 5:
    print("Aluno reprovado.")
    
elif m > 0 and m < 6.9:
    
    print("Aluno em exame.")
    n5 = float(input())
    m = (m+n5)/2
    print(f"Nota do exame: {n5:.1f}")

    if m >= 5:
        print(f"Aluno aprovado.\nMedia final: {m:.1f}")

    elif m <= 4.9:
        print(f"Aluno reprovado.\nMedia final: {m:.1f}")
    

