import sys

N, M = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline().strip() for i in range(N)]
checks = [sys.stdin.readline().strip() for i in range(M)]

sMap = { S[i] : 0 for i in range(len(S)) }

for str in checks :
    if str in sMap :
        sMap[str] += 1

print(sum(sMap.values()))
