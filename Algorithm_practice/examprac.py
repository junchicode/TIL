start = [0,0]
square = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
square[start[0]][start[1]] = 1
N = len(square)
number = 2
for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 우하좌상
    ni, nj = start[0] + di, start[1] + dj
    while 0<=ni<N and 0<=nj<N and square[ni][nj] == 0:
        square[ni][nj] = number
        number += 1
        start = [ni,nj]

print(square)