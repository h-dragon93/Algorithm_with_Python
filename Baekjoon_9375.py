case = int(input())
for i in range(case):
    n = int(input())
    items = {}
    for i in range(n):
        item, gear = input().split()
        if not gear in items:
            items[gear] = []
        items[gear].append(item)
 
    sum = 1
    for i in items:
        sum *= len(items[i]) + 1
 
    sum -= 1
    print(sum)
