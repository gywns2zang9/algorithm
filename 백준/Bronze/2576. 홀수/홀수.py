#홀수
minX = 100
sumX = 0

for _ in range(7):
    x = int(input())
    if x % 2 == 1: #홀수면
       sumX += x #합
       if x < minX:
            minX = x
if sumX == 0:
    print(-1)
else:
    print(sumX)
    print(minX)

