N = int(input())
li = []
for i in range(N) :
    a,b = map(int, input().split(" "))
    li.append([a,b])
check = []
for i in range(len(li)) :
    tmp = ([0] * (li[i][0] - 0)) + ([1]* (li[i][1] - li [i][0]))
    check.append(tmp)
max = 0
for i in range(len(li)) :
    if li[i][1] > max :
        max = li[i][1]
for i in range(len(li)) :
    add = max - li[i][1]
    check[i] = check[i] + ([0] * add)
new_max = 0
for j in range(max):
    count = 0
    for i in range(len(check)) :
        if check[i][j] == 1 :
            count += 1
    if count > new_max :
        new_max = count
print(new_max)
