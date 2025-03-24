# 마법사 상어와 비바라기
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
DS = [list(map(int, input().split())) for _ in range(M)] # [d = 방향, s = 거리]

# 방향은 8방향
# 9시 , 11시, 12시, 1시, 3시, 5시, 6시, 7시
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 설정(비바라기)
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in DS:
    ni = di[d - 1]
    nj = dj[d - 1]
    ns = s % N

    moved_clouds = []
    for i, j in clouds:
        new_i = (i + ni * ns) % N
        new_j = (j + nj * ns) % N
        moved_clouds.append((new_i, new_j))

    clouds = list(set(moved_clouds))
    for i, j in clouds:
        A[i][j] += 1

    for i, j in clouds:
        count = 0
        for k in range(4):  # 대각선만
            ni = i + di[2 * k + 1]
            nj = j + dj[2 * k + 1]
            if 0 <= ni < N and 0 <= nj < N and A[ni][nj] > 0:
                count += 1
        A[i][j] += count

    before = set(clouds)
    clouds = []

    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in before:
                A[i][j] -= 2
                clouds.append((i, j))

    before.clear()

# 결과 계산
result = sum(map(sum, A))
print(result)
