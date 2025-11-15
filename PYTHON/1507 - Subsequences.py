for w in range(int(input())):
    v = input()

    for i in range(int(input())):

        a = input()
        ind = 0

        for i in a:
            for j in range(ind,len(v)):
                if i == v[j]:
                    ind = j+1
                    break
            else:
                break
        else:
            print('Yes')
            continue
        print('No')