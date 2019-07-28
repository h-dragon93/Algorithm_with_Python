li = [0]*10
for i in range(1,10) :      # 리스트에 난쟁이들의 키를 입력 받음
    li[i] = int(input())

sum = 0
target = 100
for i in range(1, 10) :
    sum += li[i]

for i in range(1, 10) :
    for j in range(1, 10) :
        if ((sum - li[i] - li[j]) == target) :
            li[9], li[i] = li[i], li[9]
            li[8], li[j] = li[j], li[8]
li.pop()
li.pop()
li.sort()
for k in range(1, 8) :
    print(li[k])
