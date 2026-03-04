import sys
input = sys.stdin.readline

stack = []
top = -1
N = int(input())
for _ in range(N):
    commands = input().split()
    if commands[0] == 'push':
        stack.append(commands[1])
        top += 1
    elif commands[0] == 'pop':
        if top >= 0:
            print(stack.pop())
            top -= 1
        else:
            print(-1)
    elif commands[0] == 'size':
        print(top+1)
    elif commands[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif commands[0] == 'top':
        if top >= 0:
            print(stack[top])
        else:
            print(-1)