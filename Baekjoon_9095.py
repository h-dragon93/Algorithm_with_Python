dp = [0] * 100
dp[1] = 1
dp[2] = 2
dp[3] = 4
for n in range(4, len(dp)) :
    dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
m = int(input())
while m > 0 :
    i = int(input())
    print(dp[i])
    m -= 1
