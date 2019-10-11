def solution(n):
    count = 0
    for i in range(0, n//2) :
        start = i
        sum = start
        temp = 0
        while temp < n :
            sum += 1
            temp += sum
            if temp == n :
                count += 1
    return count + 1
