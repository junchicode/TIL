T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for i in range(10)]
    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                arr[i][j] += 1
    cnt = 0

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                cnt += 1

    print(f"#{tc} {cnt}")


    
     