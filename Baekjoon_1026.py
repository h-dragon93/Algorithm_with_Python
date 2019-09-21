### 최근에 다시 푼 풀이

import operator

N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

A_dict = dict(zip(range(len(A)), A))
sorted_A = sorted(A_dict.items(), key=operator.itemgetter(1))

B_dict = dict(zip(range(len(B)), B))
sorted_B = sorted(B_dict.items(), key=operator.itemgetter(1), reverse=True)

S=0
for i in range(len(sorted_A)):
    S += (sorted_B[i][1] * sorted_A[i][1])
 
print(S)


### 예전에 푼 풀이

N = int(input())
li_a = list(map(int, input().split(" ")))
li_b = list(map(int, input().split(" ")))

sum = 0
for k in range(N) :
    max, min = 0, 100

    for i in range(len(li_a)) :
        if li_a[i] > max :
            max = li_a[i]
    A = max
    li_a.remove(max)

    for i in range(len(li_b)) :
        if li_b[i] < min :
            min = li_b[i]
    B = min
    li_b.remove(min)
    sum += A*B
    
print(sum)
