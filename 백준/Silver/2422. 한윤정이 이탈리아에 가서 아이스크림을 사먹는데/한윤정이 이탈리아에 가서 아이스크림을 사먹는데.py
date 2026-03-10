import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 인덱스 에러 방지를 위해 N+1 크기로 생성
bad = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 2. 어떤 순서로 입력되어도 조회 가능하도록 양방향 저장
    bad[a][b] = True
    bad[b][a] = True

cnt = 0
# 3. i < j < k 조합 생성
for i in range(1, N - 1):
    for j in range(i + 1, N):
        # i와 j가 안 맞으면 k 루프는 진입할 필요 없음
        if bad[i][j]:
            continue 
        
        for k in range(j + 1, N + 1):
            # i-k나 j-k가 안 맞으면 이 k만 건너뛰고 다음 k 확인
            if bad[i][k] or bad[j][k]:
                continue
            
            cnt += 1

print(cnt)