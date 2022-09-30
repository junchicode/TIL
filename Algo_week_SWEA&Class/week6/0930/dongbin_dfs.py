import sys
input = sys.stdin.readline

graph = []
for i in range(4):
    list_ = list(map(int,list(input().strip())))
    graph.append(list_)

# x - 4, y - 5

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 현재로부터, 상하좌우 가능하면 움직일수 있는데, 움직였을때 0이면 2로 바꾸고(방문처리) 1이면 못움직임
# 그래프 전체를 돌면서 0인부분에서 dfs호출 (포문 두번)

def dfs(x,y,graph):
    graph[x][y] = 2 #방문처리

    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i]<4 and y+dy[i] >=0 and y+dy[i] < 5:
            if graph[x+dx[i]][y+dy[i]] == 0: #움직가능 and 방문가능 (1이면 못움직, 2도 못움직)
                dfs(x+dx[i],y+dy[i], graph)


answer = 0
for i in range(len(graph)): #행
    for j in range(5): #열
        if graph[i][j] == 0:
            dfs(i,j,graph)
            answer+=1

print(answer)