# 문제 - 미친 로봇
N, Ep, Wp, Sp, Np  = map(int, input().split())

arr = [[0] * (2*N+1) for _ in range(2*N+1)] # N,N이 중앙에 오도록
list_p = [Ep, Wp, Sp, Np]

dx = [1, -1, 0, 0] # 동서남북
dy = [0, 0, -1, 1]

result = 0

def dfs( x, y, cnt, percent):
    global result

    if cnt == N: # 종료
        result += percent
        return

    arr[x][y] = 1 # 현재 위치

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2*N+1 and 0 <= ny < 2*N+1:
            if arr[nx][ny] == 0:
                dfs(nx, ny, cnt+1, percent*list_p[i] / 100)

    arr[x][y] = 0

dfs(N, N, 0, 1)
print(result)