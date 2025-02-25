from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 동남서북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = [[False] * m for _ in range(n)]

cnt = 0 #개수
max_width = 0 #넓이

def bfs(start):
    global max_width

    i, j = start
    queue = deque([(i, j)])
    visited[i][j] = True # 시작점 방문 찍고
    width = 1

    while queue:
        cur_i, cur_j = queue.popleft() # 현재 위치 가져와서
        # 4방향 탐색
        for k in range(4):
            ni, nj = cur_i+di[k], cur_j+dj[k]
            # 범위 속하는지 보기
            if 0 <= ni < n and 0 <= nj < m:
                # 탐색안한 곳인지, 갈 수 있는 곳인지 확인
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    width += 1
                    queue.append((ni, nj))

    max_width = max(width, max_width)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs((i, j))

print(cnt, max_width)