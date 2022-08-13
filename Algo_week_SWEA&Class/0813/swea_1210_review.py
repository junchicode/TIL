import sys

sys.stdin = open('input.txt', 'r')

# 역순으로 거슬러 올라가는 델타 
# 좌 우 상 
dx = [0, 0, -1]
dy = [-1, 1, 0]

for _ in range(1, 11):
    '''
    100 * 100  사다리 보드 
    도착점 2 
    반환 값이 출발지인 X 의 인덱스
    0으로 채워졌고 사다리는 1  
    '''
    tc = int(input())
    # 사다리 보드 
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(100):
        # 마지막줄에서 2 찾기 
        if ladder[99][i] == 2:
            x = 99 
            y = i 
    #print(f'x : {x}, y : {y}')

    while x != 0:
        for j in range(3):
            # 델타 좌표 설정
            wx = x + dx[j]
            wy = y + dy[j]

            if 0 <= wx < 100 and 0 <= wy < 100 and ladder[wx][wy] == 1:
                ladder[wx][wy] = 0 # 0으로 초기화하면 다시 3방향 탐색할 때 탐색할 필요가 없어짐

                x = wx # x초기화
                y = wy # y초기화
    print(f'#{tc} {y}')
