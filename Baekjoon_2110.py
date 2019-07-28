import sys

N, C = map(int, sys.stdin.readline().split(" "))
house = []
for i in range(N) :
    house.append(int(sys.stdin.readline()))
house.sort()

def possible(dist) :

    cnt = 1
    prev = house [0]

    for i in range(N) :
        if house[i] - prev >= dist :
            cnt += 1
            prev = house[i]
    if cnt >= C :
        return True
    return False

low = 1
result = 0
high = house[N-1] - house[0]

while low <= high :
    mid = int((low + high) / 2)
    ok = possible(mid)
    if ok :
        result = max(result, mid)
        low = mid + 1
    else :
        high = mid - 1

print(result)
