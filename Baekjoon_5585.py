coin = int(input())
dp = [0] * (1000-coin + 1)

for i in range(len(dp)) :
    dp[i] = i 

for i in range(5,len(dp)) :
    dp[i] = min(dp[i], dp[i-5]+1)

for i in range(10, len(dp)) :
    dp[i] = min(dp[i], dp[i - 10] + 1)

for i in range(50, len(dp)) :
    dp[i] = min(dp[i], dp[i - 50] + 1)

for i in range(100, len(dp)) :
    dp[i] = min(dp[i], dp[i - 100] + 1)

for i in range(500, len(dp)) :
    dp[i] = min(dp[i], dp[i - 500] + 1)
print(dp[1000-coin])
