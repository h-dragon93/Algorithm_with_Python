def solution(jobs):
    import heapq

jobs.sort()
    answer = 0
    n = 0
    time = jobs[0][0]
    pq = []
    
    while jobs:
        (request, expend) = jobs.pop(0)
        n += 1
        time += expend
        answer += (time - request)
                while jobs and jobs[0][0] < time:
            (request, expend) = jobs.pop(0)
            heapq.heappush(pq, (-expend, request))

        while pq:
            (expend, request) = heapq.heappop(pq)
            jobs.insert(0, [request, -expend])

    answer //= n
    return answer
