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
