li = []
count = 0
N, K = map(int, input().split(' '))
for i in range(N):
    a = int(input())
    li.append(a)
li.sort(reverse = True)
for i in range(len(li)) :
    count += K//li[i]
    K %= li[i]
    
print(count)
