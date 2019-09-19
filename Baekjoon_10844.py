n = int(input())
dp = [0] + [1]*9
for _ in range(1, n) :
    temp = [0] * 10
    temp[0], temp[9] = dp[1], dp[8]
    for i in range(1,9) :
        temp[i] = dp[i-1] + dp[i+1]
    dp = temp
print(sum(dp)%1000000000)
