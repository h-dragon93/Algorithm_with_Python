coin = int(input())
dp = [0] * (coin + 1)
for i in range(len(dp)) :
    if i % 3 :
        dp[i] = float("INF")
    else :
        dp[i] = i // 3

for i in range(5, len(dp)) :
    if i % 5 :
        dp[i] = min(dp[i], dp[i-5]+1)
    else :
        dp[i] = i // 5

for i in range(len(dp)) :
    if dp[i] == float("INF"):
        dp[i] = -1
print(dp[coin])
