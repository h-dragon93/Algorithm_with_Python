import sys

N = int(sys.stdin.readline())
li=[]
for i in range(N):
    li.append(int(input()))
li = sorted(li, reverse= True)
max = li[0]
for i in range(len(li)-1) :
    if (li[i+1] * (i+2)) > max :
        max = li[i+1] * (i+2)

print(max)
