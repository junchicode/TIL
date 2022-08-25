def bfs(start,N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        start = q.pop(0)
        if maze[start[0]][start[1]] == 3:
            return 1
        
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = start[0]+di, start[1] + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni,nj])
                visited[ni][nj] = 1
        
    return 0

T = 10
for i in range(T):
    qnumber = int(input())
    maze= [list(map(int, input())) for _ in range(16)]
    for i in range(16):

        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                end = [i, j]
            else:
                pass
    start = [1,1]
    end = [13,13]
    

    print(f"#{qnumber} {bfs(start, 16)}")
    
    
    
    

