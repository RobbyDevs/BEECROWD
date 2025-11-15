hi,hf = map(int,input().split())

if hi > hf:
    h = 24- abs(hi - hf)
    print(f"O JOGO DUROU {h} HORA(S)")

elif hi < hf:
    print(f"O JOGO DUROU {abs(hi-hf)} HORA(S)")

else:
    print(f"O JOGO DUROU 24 HORA(S)")