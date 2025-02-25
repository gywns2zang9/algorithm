#미로 탐색
from collections import deque

N, M = map(int, input().split())
arr = [[*(input())] for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = [[False] * M for _ in range(N)]

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        cur_i, cur_j, cnt = queue.popleft()

        if cur_i == (N-1) and cur_j == (M-1):
            return cnt

        for k in range(4):
            ni, nj = cur_i + di[k], cur_j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '1' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj, cnt + 1))


print(bfs())


