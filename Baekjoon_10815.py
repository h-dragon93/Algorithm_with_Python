import sys

N = int(input())
li_N = list(map(int, sys.stdin.readline().split(" ")))
M = int(input())
li_M = list(map(int, sys.stdin.readline().split(" ")))

li_N.sort()


for i in li_M :
    left = 0
    right = N - 1
    while left <= right :
        mid = int((left+right)/2)
        if i > li_N[mid] :
            left = mid + 1
            continue
        elif i < li_N[mid] :
            right = mid - 1
            continue
        else :
            print(1, end=" ")
            break

    if left > right :
        print(0, end = " ")
