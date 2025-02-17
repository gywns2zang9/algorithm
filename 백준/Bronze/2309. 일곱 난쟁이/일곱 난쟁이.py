#일곱 난쟁이
dwarfs = sorted([int(input()) for _ in range(9)])

gapDwarfs = sum(dwarfs) - 100
tkn = 0

for i in range(9):
    if tkn == 1:
        break
    for j in range(i+1, 9):
        if tkn == 1:
            break
        elif dwarfs[i] + dwarfs[j] == gapDwarfs:
            dwarfs[i], dwarfs[j] = 0, 0
            tkn = 1

for k in range(9):
    if dwarfs[k] != 0:
        print(dwarfs[k])