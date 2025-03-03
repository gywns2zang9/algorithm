dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

N = int(input())

for n in range(2, N+1):
    for i in range(10):
        if i == 0:
            dp[n][i] = dp[n-1][1]
        elif i == 9:
            dp[n][i] = dp[n-1][8]
        else:
            dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]

print(sum(dp[N])%1000000000)