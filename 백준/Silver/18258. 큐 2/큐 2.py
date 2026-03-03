import sys
from collections import deque

input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    commands = input().split()

    if commands[0] == 'push': # push X: 정수 X를 큐에 넣는 연산이다.
        q.append(commands[1])
    elif commands[0] == 'pop': # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif commands[0] == 'size': # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(q))
    elif commands[0] == 'empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == 'front': # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif commands[0] == 'back': # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(q) == 0:
            print(-1)
        else: 
            print(q[-1])