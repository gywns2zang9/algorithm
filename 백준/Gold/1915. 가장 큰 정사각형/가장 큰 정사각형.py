# 가장 큰 정사각형
N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]

for x in range(N):
    for y in range(M):
        A[x][y] = int(A[x][y])

for i in range(1, N):
    for j in range(1, M):
        a = A[i][j-1]
        b = A[i-1][j-1]
        c = A[i-1][j]
        if 0 < min(a, b, c) and A[i][j] > 0:
            A[i][j] = min(a, b, c) + 1

max_width = A[0][0]

for n in range(N):
    for m in range(M):
        max_width = max(max_width, A[n][m])
print(max_width* max_width)