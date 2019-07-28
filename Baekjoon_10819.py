from itertools import permutations

n = int(input())
a = permutations(sorted(list(map(int, input().split()))))
ans = 0

for k in a:
    sums = 0
    for i in range(n-1):
        sums += abs(k[i]-k[i+1])
    ans = max(ans, sums)
    
print(ans)
