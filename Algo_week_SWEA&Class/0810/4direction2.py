N = 3
M = 4

for i in range(N):
    for j in range(M):
        for di, dj in [[0,1],[1,0],[0,1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)