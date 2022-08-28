def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >=  n:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
# 4,5
'''
00110
00011
11111
00000'''
graph = [list(map(int, input())) for _ in range(n)]

res = 0 

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            res += 1
print(graph)

