n = int(input())
k = n
count = 0

while True :
    if n < 10 :
        n = n*11
        count += 1
        if k == n:
            break
        continue
    n = ((n % 10) * 10) + (((n % 10)+(n // 10))%10)
    count += 1
    if k == n :
        break
print(count)
