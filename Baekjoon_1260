import sys

N, M, V = map(int, sys.stdin.readline().split())
li = []
for i in range(M) :
    li.append(list(map(int, sys.stdin.readline().split())))

graph = [[] for _ in range(N)]

for (a, b) in li:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def bfs(graph, start) :
    visited = []
    queue = [start]
    while queue :
        n = queue.pop(0)
        if n not in visited :
            visited.append(n)
            tmp = []
            for i in graph[n] :
                if i not in visited :
                    tmp.append(i)
            tmp.sort()
            queue = queue+tmp
    return visited

def dfs(graph, start):
    visited = []
    stack=[start]
    while stack:
        n=stack.pop()
        if n not in visited:
            visited.append(n)
            tmp = []
            for i in graph[n]:
                if i not in visited :
                    tmp.append(i)
            tmp.sort(reverse=True)

            stack = stack + tmp

    return visited

li_dfs = dfs(graph,V-1)
li_bfs = bfs(graph,V-1)

for i in range(len(li_dfs)) :
    li_dfs[i] += 1
    li_bfs[i] += 1

print(" ".join(list(map(str, li_dfs))))
print(" ".join(list(map(str, li_bfs))))
