import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    PS = input()
    stack = []
    top = -1
    for s in PS:
        if s == '(':
            stack.append(s)
            top += 1
        elif s == ')':
            if len(stack) > 0:
                if stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    stack.append(s)
            else:
                stack.append(s)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')