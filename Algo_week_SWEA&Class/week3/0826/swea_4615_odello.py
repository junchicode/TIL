def delta(bd1, bd2, color, N):
    
    board[bd1][bd2] = color
    for di, dj in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
        ni, nj = bd1 + di, bd2 + dj
        flip = []
        while True:
            if ni < 0 or nj < 0 or ni > N-1 or nj > N-1:
                flip = []
                break
            if board[ni][nj] == 0:
                flip = []
                break
            if board[ni][nj] == color:
                break
            else:
                flip.append([ni, nj])
            ni, nj = ni + di, nj + dj
        
        for fi, fj in flip:
            if color == 1:
                board[fi][fj] = 1
            else:
                board[fi][fj] = 2

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    for i in range(N//2-1, N//2+1):
        for j in range(N//2-1, N//2+1):
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1

    for i in range(M):
        bd1,bd2,color = map(int, input().split())
        bd1, bd2 = bd1-1, bd2-1
        delta(bd1, bd2, color, N)
    white = 0
    black = 0
    for i in board:
        for j in i:
            if j == 1:
                white += 1
            elif j == 2:
                black += 1
            else:
                pass
            
    print(f"#{tc} {white} {black}")
                
      
        