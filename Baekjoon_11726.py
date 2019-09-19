n = int(input())
li = [0]* (n+1)

if n == 1 :
    li[1] = 1
if n == 2 :
    li[2] = 2
if n>=3 :
    li[1] = 1
    li[2] = 2
    li[3] = 3
    for i in range(3, n + 1):
        li[i] = li[i - 1] + li[i - 2]

print(li[n]%10007)
