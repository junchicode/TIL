N= int(input())
m = [list(map(int, input())) for _ in range(N)]

starti = 0
startj = 0 
for i in range(N):
    for j in range(N):
        if m[i][j] == 2:
            starti = i
            startj = j
            break
        
def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append([i,j])
    visited[i][j] = 1
    while q: 
        i, j = q.pop(0)
        # 도착점인가?
        if m[i][j] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and m[ni][nj] != 1 and visited[ni][nj] ==0:
                q.append([ni,nj])
                visited[ni][nj] = visited[i][j] + 1
        return 0     