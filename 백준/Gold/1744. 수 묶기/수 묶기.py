N = int(input())
lst = sorted([int(input()) for _ in range(N)])

zero = False # 0
one = 0 # 1
plus = [] # 2 이상
minus = [] # 음수

for i in range(N):
    if lst[i] < 0:
        minus.append(lst[i])
    elif lst[i] == 0:
        zero = True
    elif lst[i] == 1:
        one += 1
    elif lst[i] > 1:
        plus.append(lst[i])

result = 0

plus.reverse()
if len(plus) > 0:
    if len(plus) % 2 == 0:
        for i in range(0, len(plus), 2):
            result += plus[i] * plus[i + 1]
    else:
        for j in range(0, len(plus) - 1, 2):
            result += plus[j] * plus[j + 1]
        result += plus[-1]

# 음수 부분
if len(minus) > 1:
    if len(minus) % 2 == 0:
        for i in range(0, len(minus), 2):
            result += minus[i] * minus[i + 1]

    else:
        for j in range(0, len(minus) - 1, 2):
            result += minus[j] * minus[j + 1]
        if not zero:
            result += minus[-1]

elif len(minus) == 1:
    if not zero:
        result += minus[0]


print(result + one)