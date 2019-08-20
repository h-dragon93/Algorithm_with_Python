def bfs(v) :
    queue = []
    queue.append(v)
    visited[v] = True
    cnt = 0
    while queue :
        v = queue.pop(0)
        for e in graph[v] :
            if not visited[e] :
                visited[e] = True
                queue.append(e)
                cnt += 1
    return cnt
## 입력
V = int(input())
E = int(input())
graph = [ [] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
for _ in range(E) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1))
