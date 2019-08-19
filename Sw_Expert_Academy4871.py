def DFS(start, end_node):
    global result
    visited[start] = 1
    #print("visited", visited)
    for next in range(1, V + 1):
        if graph[start][next] and not visited[next]:
            if next == end_node:
                result = 1
                return
            DFS(next, end_node)
    return

T = int(input())
for test_case in range(1, T+1):
    V,E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E) :
        start, end = map(int, input().split())
        graph[start][end] = 1
    start_node, end_node = map(int, input().split())
    result = 0
    DFS(start_node, end_node)
    print('#{0} {1}'.format(test_case, result))
