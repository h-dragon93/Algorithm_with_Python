from collections import deque

def solution(x, y, n):
    queue = deque([(y, 0)])

    while queue:
        y, count = queue.popleft()
        
        if x == y:
            return count
        if x > y:
            continue
        count += 1
        if y % 2 == 0:
            queue.append([y // 2, count])
        if x * 3 <= y:
            queue.append([y // 3, count])
        queue.append([y - n, count])
        

    return -1
