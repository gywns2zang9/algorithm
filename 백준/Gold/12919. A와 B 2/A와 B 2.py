# A와 B 2

S = input() # 1 ≤ S의 길이 ≤ 49
T = input() # 2 ≤ T의 길이 ≤ 50, S의 길이 < T의 길이

result = 0

def AB2(t):
    global result

    if t == S:
        result = 1
        return

    if len(t) <= 0:
        return

    if t[len(t)-1] == 'A':
        AB2(t[:-1])
    if t[0] == 'B':
        AB2(t[1:][::-1])

AB2(T)
print(result)