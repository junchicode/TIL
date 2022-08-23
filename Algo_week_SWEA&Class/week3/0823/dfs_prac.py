def search(lst, x, y, visited):
    global check_answer
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<len(lst) and 0<=ny<len(lst) and not visited[nx][ny]:
            visited[nx][ny] = True
            if lst[nx][ny] == 3:
                check_answer = True
            elif lst[nx][ny] == 0:
                search(lst, nx, ny, visited)

size = int(input())
maze = [list(map(int, input())) for _ in range(size)]
x = size - 1
y = 0
for i in maze[x]:
    if i == 2:
        break
    else: 
        y += 1
        
visited = [[False for _ in range(size)] for _ in range(size)]
check_answer = False

search(maze, x, y, visited)

if check_answer:
    print("ya")
else:
    print("fuck")



    
