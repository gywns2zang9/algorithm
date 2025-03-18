# 문자열 폭발
A = input()
B = input()

def boom(A, B):
    stack = []
    boom_len = len(B)

    for a in A:
        stack.append(a)

        if len(stack) >= boom_len and "".join(stack[-boom_len:]) == B:
            del stack[-boom_len:]

    if stack:
        print("".join(stack))
    else:
        print("FRULA")

boom(A, B)
