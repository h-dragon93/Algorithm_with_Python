m = int(input())
dp = [0] * 101
answer = [0] * 101
dp[0], dp[1], dp[2] , dp[3], dp[4] = 0,1,1,1,2
dp[5], dp[6], dp[7] , dp[8], dp[9] = 2,3,4,5,7
for i in range(m):
    n = int(input())
    if n < 7 :
        answer[i] = dp[n]
        continue
    for j in range(7, n+1) :
        dp[j] = dp[j - 5] + dp[j - 1]
    answer[i] = dp[n]

for i in range(m) :
    print(answer[i])
