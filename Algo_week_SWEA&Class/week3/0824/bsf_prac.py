def bfs(G, v):
    visited = [0]*(n+1)
    q = []
    q.append(v)
    while q:
        t = q.pop(0)
        if not visited[t]:
            visited[t] = True
            visit(t)
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                
                
