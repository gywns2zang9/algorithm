def bfs(maps):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = [[0, 0, 1]]
    result = -1
    while q:
        now = q.pop(0)
        now_i, now_j, cnt = now[0], now[1], now[2]
        print(now)
        if now_i == n-1 and now_j == m-1:
            result = cnt
            break
        for k in range(4):
            new_i = now_i + di[k]
            new_j = now_j + dj[k]
            if 0 <= new_i < n and 0 <= new_j < m:
                if maps[new_i][new_j] == 1 and visited[new_i][new_j] == False:
                    visited[new_i][new_j] = True
                    q.append([new_i, new_j, cnt+1])
    return result

def solution(maps):
    answer = 0
    answer = bfs(maps)
    return answer