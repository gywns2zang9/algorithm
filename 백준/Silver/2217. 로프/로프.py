#로프
N = int(input())
A = sorted([int(input()) for _ in range(N)])

maximum = 0

for n in range(N):
    if A[n]*(N-n) > maximum:
        maximum = A[n] * (N - n)
print(maximum)
