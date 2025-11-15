A, B, C = map(int, input().split())

if A > B and A > C:
    print(f"{A} eh o maior")

elif B > A and B > C:
    print(f"{B} eh o maior")

elif C > B and C > A:
    print(f"{C} eh o maior")

else:
    print(f"{B} eh o maior")