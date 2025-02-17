#핸드폰 요금
N = int(input())
calls = list(map(int, input().split()))

sumY = 0
sumM = 0

for i in range(N):
    x = calls[i] // 30 + 1
    sumY += 10*x
    y = calls[i] // 60 + 1
    sumM += 15*y

if sumM == sumY:
    print("Y", "M", sumY)
elif sumM < sumY:
    print("M", sumM)
else:
    print("Y", sumY)

