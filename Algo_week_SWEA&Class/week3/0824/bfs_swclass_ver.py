def bfs(G, v, n):       # n = 정점의 개수
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        visit(t)        # 해줄걸 하는데 만약 0 -> 99라면 혹시 t가 99니?
                        # 방문하는 정점 순서를 알고싶어? print(t)
        
        for i in G[t]:  # 얘랑 인접한 원소들 i나 w는 같아
            if not visited[i]:
                q.append(i)
                visited[i] = visited[n] + 1 # visited = [1,2,2,2,3,3,3,3]