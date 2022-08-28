def dt(cur,i, j, d):
    global fly
    y = i + d[0]
    x = j + d[1]
    
    if cur == M-1 or not 0 <= x < N or not 0 <= y < N:
        return
    
    fly += arr[y][x]
    dt(cur + 1, y, x, d)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
    
D =  [[(0, 1), (1, 0), (0, -1), (-1, 0)], [(1, 1), (1, -1), (-1, -1), (-1, 1)]]
    
for i in range(N):
    for j in range(N):
        for delta in D:
            fly = arr[i][j]
            for d in delta:
                dt(0,i, j, d)
            print(fly)
            
