def bfs(v, N, t):                           # 시작, 마지막 정점 번호, 타겟
    visited = [0]*(N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q: 
        v = q.pop(0)
        if v == t:
            return 1                        # 타겟 발견
        for w in adjlist[v]:
            q.append(w)
            visited[w] = visited[v] + 1
    return 0

T = 1
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    
    adjlist = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjlist[a].append(b)                # 단방향
        
    bfs(0, 99, 99)                          # 시작, 마지막 정점, 
    
    
    