N = int(input())
li = list(map(int,input().split()))
li_new = [0]*N

for i in range(N) :
    count = 0
    for j in range(N) :
        if (count == li[i] and li_new[j] == 0) :
            li_new[j] = i+1
            break
        if li_new[j] == 0 :
            count += 1
for i in range(N) :
    print(li_new[i], end = " ")
