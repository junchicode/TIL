N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _  in range(N)]

res = 0
for i in range(N):
    cnt = 0
    for r in range(N):
        if arr[i][r] == 1:
            cnt += 1
        if arr[i][r] == 0 or r == N - 1: # 0이거나 끝에 도달할 때만 
            if cnt == K:
                res += 1
            cnt = 0 
    for c in range(N):
        if arr[c][i] == 1:
            cnt += 1
        if arr[c][i] == 0 or c == N - 1:
            if cnt == K:
                res += 1
            cnt = 0        
print(res)
        
       
            
        
            
            
            
            