hi,mi,hf,mf = map(int,input().split())

ti = (hi*60)+mi
tf = (hf*60)+mf
t = 1440

if tf>ti:
    t = tf-ti    
elif tf<ti:
    t = 1440 - (ti-tf)
    


h = t//60
m = (t%60)
print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")