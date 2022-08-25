def bfs(S, E, graph):
    q = [S]
    visited[S] = 1
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

            if i == E:
                return visited[i] - 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    S, E = map(int, input().split())
    answer = bfs(S, E, graph)
    print('#{} {}'.format(tc, answer))