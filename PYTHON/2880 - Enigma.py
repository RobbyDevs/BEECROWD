cif = input()
crib = input()

p = 0
crib_len = len(crib)
cif_len = len(cif)

for it in range(cif_len - crib_len + 1):
    fit = all(crib[i] != cif[it + i] for i in range(crib_len))
    if fit:
        p += 1

print(p)