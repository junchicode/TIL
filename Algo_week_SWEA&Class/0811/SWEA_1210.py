for _ in range(10):
    t = int(input())
		
		# 배열 생성할때 양옆에 [0]을 추가 (패딩)
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for i in range(102):  # 마지막 줄의 X위치 검색
        if arr[99][i] == 2:
            X = i
    Y = 99  # 뒤에서부터 거꾸로 올라갈 예정

    while True:
        if Y == 0:  # 맨 윗줄에 도착하면 while문 탈출
            break
        if arr[Y][X+1] == 1:  # 오른쪽에 1이 있는경우 계속 이동
            while arr[Y][X+1]:
                X += 1
        elif arr[Y][X-1] == 1:  # 왼쪽에 1이 있는경우 계속 이동
            while arr[Y][X-1]:
                X -= 1
        Y -= 1  # 한줄 위로 이동

    print(f'#{t} {X-1}')  # 처음에 앞에 0을 추가해줬으므로 좌표는 X-1
        
    
    