va = int(input())


while True:
    worked = False
    
    try:
         v = int(input())
         worked = True
         if v <= va:
              print(va+1)
              break
         va = v

    except EOFError:
        if worked == False:
             print(va+1)
        break