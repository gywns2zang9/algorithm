N = int(input())

# 버리고, 아래로 -> 선입선출
from collections import deque
arr = deque([i for i in range(1, N+1)])

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

print(*arr)