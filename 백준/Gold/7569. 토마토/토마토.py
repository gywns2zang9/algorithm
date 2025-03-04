from collections import deque

M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N*H)]

q = deque()
visited = [[False] * M for _ in range(N*H)]

for nh in range(N*H):
    for m in range(M):
        if arr[nh][m] == 1:
            visited[nh][m] = True
            q.append((nh, m, 0))

di = [0, 1, 0, -1, 0, 0]
dj = [1, 0, -1, 0, 0, 0]
dk = [0, 0, 0, 0, N, -N]

di_top = [0, 1, 0, 0, 0, 0]
di_bot = [0, 0, 0, -1, 0, 0]

max_time = 0

while q:
    cur_i, cur_j, time = q.popleft()
    for r in range(6):
        if (cur_i+1) % N == 0:
            new_i = cur_i + di_bot[r] + dk[r]
        elif (cur_i+1) % N == 1:
            new_i = cur_i + di_top[r] + dk[r]
        else:
            new_i = cur_i + di[r] + dk[r]
        new_j = cur_j + dj[r]
        if 0 <= new_i < N * H and 0 <= new_j < M and not visited[new_i][new_j]:
            if arr[new_i][new_j] == 0:
                visited[new_i][new_j] = True
                max_time = time+1
                q.append((new_i, new_j, time+1))


for i in range(N*H):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == False:
            max_time = -1

print(max_time)
