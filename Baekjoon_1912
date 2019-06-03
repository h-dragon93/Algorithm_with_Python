import sys

li = []
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dp = [0]*n

dp[0] = li[0]
tmp = dp[0]
for i in range(1, len(li)) :

    dp[i] = max(dp[i-1]+li[i], li[i])
    tmp = max(dp[i], tmp)

print(tmp)
