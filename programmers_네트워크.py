def bfs(graph, start) :
    visit = list()
    queue = list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def make_graph(n, computers) :
    graph = { node : [] for node in range(n) }
    for i in range(n) :
        for j in range(n) :
            if i == j :
                continue
            if computers[i][j] and i not in graph :
                graph[i] = [j]
            elif computers[i][j] and j not in graph[i] :
                graph[i].append(j)
    return graph

def solution(n, computers):

    graph = make_graph(n, computers)
    tmp = []
    for i in range(n) :
        if i in graph :
            a = bfs(graph, i)
            tmp.append(a)
    paths = map(sorted, tmp)
    a = set(["".join(map(str, path)) for path in paths])
    
    return len(a)
