import sys
N = int(sys.stdin.readline())

dp = [ [] for _ in range(N+1)]

dp[1].append(0)
dp[1].append(1)

for i in range(2, N+1) :
    dp[i].append(dp[i-1][0] + dp[i-1][1])
    dp[i].append(dp[i-1][0])

print(dp[N][0] + dp[N][1])
