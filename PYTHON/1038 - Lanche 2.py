c,q = map(int,input().split())

card = [4.00,4.50,5.00,2.00,1.50,0.0]

print(f"Total: R$ {(card[c-1]*q):.2f}")