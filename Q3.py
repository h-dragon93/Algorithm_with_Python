count = 0

def DFS (numbers, target, value, idx ) :
    global count
    N = len(numbers)
    if idx ==  N and target == value :
        count += 1
        return
    if idx == N :
        return

    DFS(numbers, target,  value + numbers[idx], idx+1)
    DFS(numbers, target,  value - numbers[idx], idx+1)

def solution(numbers, target) :
    global count
    DFS(numbers, target, 0, 0)
    return count

solution([1,1,1,1,1], 3)
print(count)
