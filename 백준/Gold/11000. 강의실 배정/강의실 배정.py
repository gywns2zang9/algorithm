import heapq

N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])

q = []
heapq.heappush(q, lst[0][1]) # 첫 수업 끝나는 시간 삽입

for i in range(1, N):
    # 현재 강의 시작 시간 >= 가장 빨리 끝나는 강의실
    if lst[i][0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, lst[i][1])

print(len(q))