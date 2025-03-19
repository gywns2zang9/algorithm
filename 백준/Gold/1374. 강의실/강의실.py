# 강의실
import heapq
# 이거 우선 순위 큐? 비슷한 문제를 풀었던거 같음

N = int(input()) # 강의의 개수
# lectures = sorted([list(map(int, input().split())) for _ in range(N)])
# print(lectures) # [[1, 3, 8], [2, 7, 13], [3, 2, 14], [4, 12, 18], [5, 6, 20], [6, 15, 21], [7, 20, 25], [8, 6, 27]]
lectures = []
max_time = 0
for _ in range(N):
    n, start, end = map(int, input().split())
    if end >= max_time:
        max_time = end
    lectures.append([start, end])
lectures.sort()
# print(lectures) # [[2, 14], [3, 8], [6, 20], [6, 27], [7, 13], [12, 18], [15, 21], [20, 25]]

# ...그 먼저 시작하는 순으로 넣고 끝나는 순으로 뺐던거 같은데..

# 첫 번째 아이디어
# 걍 수업시간 체크해서 가장 큰 값 찾기?

# times = [0]* max_time
# # print(times)
# for lecture in lectures:
#     start, end = lecture[0], lecture[1]
#     for time in range(start, end):
#         times[time] += 1
# print(times) # [0, 0, 1, 2, 2, 2, 4, 5, 4, 4, 4, 4, 5, 4, 3, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1]
# print(max(times)) # 5
# 메모리 초과

queue = []
heapq.heappush(queue, lectures[0][1])

for n in range(1, N):
    # 시작 시간을 기준으로 넣고,,
    # 넣을 땐 끝나는 시간을 담아놓고,,
    # 시작 시간이 가장 먼저 끝나는 끝나는 시간이랑 비교해서 빼고 넣고,,
    if lectures[n][0] >= queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue,lectures[n][1])
    else:
        heapq.heappush(queue, lectures[n][1])

print(len(queue))