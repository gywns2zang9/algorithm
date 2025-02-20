# from collections import deque
# def bfs(start):
#     queue = deque([start])
#     visited =
#     queue.popleft()

# 숨바꼭질
# N = 수빈, K = 동생
N, K = map(int, input().split())

q = [[N, 0]]
visited = [0] * 100001

while len(q) > 0: #q가 남아있으면
    now, cnt = q.pop(0)
    if now == K:
        print(cnt)
        break

    else:
        if 0 <= now-1 <= 100000 and visited[now-1] == 0:
            visited[now-1] = 1
            q.append([now-1, cnt+1])

        if 0 <= now + 1 <= 100000 and visited[now+1] == 0:
            visited[now+1] = 1
            q.append([now+1, cnt+1])
        if 0 <= now*2 <= 100000 and visited[now*2] == 0:
            visited[now*2] = 1
            q.append([now*2, cnt+1])
