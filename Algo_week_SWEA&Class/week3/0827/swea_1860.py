T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = sorted(list(map(int, input().split())))
    timeline = [0]*(customers[-1]+2) #0,1,2,3,4,0

    for c in customers:
        for i in range(c, len(timeline)):
            timeline[i] -= 1
    tmp = 0
    for i in range(len(timeline)):
        if i >= M and i%M == 0:
            tmp += K
        timeline[i] += tmp

    result = True
    for c in customers:
        if timeline[c] < 0:
            result = False
        else:
            pass
            
    
    if result == True:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")

    
