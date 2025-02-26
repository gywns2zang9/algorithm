from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
visited = [[False]*M for _ in range(N)]

for n in range(N):
    for m in range(M):
        # 익은 토마토 자리 queue 미리 보내고 방문처리
        if arr[n][m] == 1:
            start = [n, m, 0]
            queue.append(start)
            visited[n][m] = True
        # 토마토가 없는 자리는 그냥 미리 방문처리
        elif arr[n][m] == -1:
            visited[n][m] = True

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    cnt = 0
    while queue:
        i, j, cnt = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and arr[ni][nj] == 0:
                    visited[ni][nj] = True
                    queue.append((ni, nj, cnt+1))

    return cnt

result = bfs()

for n1 in range(N):
    for m1 in range(M):
        if visited[n1][m1] == False:
            result = -1
            break

print(result)