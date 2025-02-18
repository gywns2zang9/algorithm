N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = list([0]* (i+1) for i in range(N))
dp[0][0] = arr[0][0]

for n in range(1, N):
    for idx in range(n+1):
        if idx == 0:
            dp[n][idx] = dp[n-1][idx] + arr[n][idx]
        elif idx == n:
            dp[n][idx] = dp[n-1][idx-1] + arr[n][idx]
        else:
            if dp[n-1][idx-1] > dp[n-1][idx]:
                dp[n][idx] = dp[n-1][idx-1] + arr[n][idx]
            else:
                dp[n][idx] = dp[n-1][idx] + arr[n][idx]

print(max(dp[N-1]))
