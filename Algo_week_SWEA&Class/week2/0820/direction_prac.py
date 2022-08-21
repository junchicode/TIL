
ladder = [
    [0,0,1,0,0],
    [0,0,1,1,0],
    [0,0,0,1,1],
    [0,0,0,0,1],
    [0,0,0,0,2]
    ]

dx = [0, 0, -1]
dy = [-1, 1, 0]


for i in range(5):
        # 마지막줄에서 2 찾기 
    if ladder[4][i] == 2:
        x = 4
        y = i 
    #print(f'x : {x}, y : {y}')
print(y)
cnt = 0
while x != 0:
    for j in range(3):
            # 델타 좌표 설정
        wx = x + dx[j]
        wy = y + dy[j]

        if 0 <= wx < 5 and 0 <= wy < 5 and ladder[wx][wy] == 1:
            ladder[wx][wy] = 0
            cnt += 1

            x = wx 
            y = wy 
print(y)
print(cnt)

    
