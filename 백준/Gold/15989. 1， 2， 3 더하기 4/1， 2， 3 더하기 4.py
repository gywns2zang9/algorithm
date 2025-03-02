dp = [1] * 10001  # 1의 합으로 나타낼 수 있기때문

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]


T = int(input())
for t in range(T):
    N = int(input())
    print(dp[N])