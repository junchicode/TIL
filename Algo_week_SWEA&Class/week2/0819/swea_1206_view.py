
T = 10
for tc in range(1, T+1):
    size = int(input())
    blds = list(map(int, input().split()))
    res = 0
    for i in range(size-5+1):
        fiveblds = []
        for j in range(5):
            fiveblds.append(blds[i+j])
            
        if fiveblds[2] == max(fiveblds):
            srtfive = sorted(fiveblds)
            diff = fiveblds[2] - srtfive[-2]
            if diff > 0:
                res += diff
            
    print(f"#{tc} {res}")