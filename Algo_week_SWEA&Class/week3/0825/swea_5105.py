def bfs(start, maze):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        start = q.pop(0)
        if maze[start[0]][start[1]] == 3:
            return visited[start[0]][start[1]]-2
        
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj = start[0] + di, start[1] + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[start[0]][start[1]] + 1
    
    return 0
T = int(input())
for tc in range(1, T+1):   
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i,j]
                
    print(f"#{tc} {bfs(start, maze)}")
