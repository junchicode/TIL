N = int(input())
bdlist = list(map(int, input().split()))
res = 0
for i in range(2, N-2): # 옆 00 00
    tmp = bdlist[i] # 현재 건물 지정
    tmpn = 257 # 왼옆옆 오옆옆이랑 비교하기 위한 tmpn
    for j in range(i-2, i+3): # tmp를 포함한 왼옆옆 오옆옆 범위
        if j == i: #tmp값 pass
            pass
        else:
            if tmp - bdlist[j] < tmpn: # tmp에서 다른 위치 값 뺀게 tmpn보다 작다면
                tmpn = tmp - bdlist[j] # tmpn은 위에 값으로 초기화
    
    if tmpn > 0: # tmpn이 0보다 크면
        res += tmpn # res에 더해줌
        
print(res)
# 단순히 현재 기둥 기준으로 왼오 두개씩 비교해가면 답이 도출된다