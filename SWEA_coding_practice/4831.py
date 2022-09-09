K, N, M = map(int, input().split())
arr = [0]*(N+1)
charger = map(int, input().split())
for i in charger:
    arr[i] = 1
start = 0
cur = 0 + K
cnt = 0
while cur < N:
    if arr[cur] == 1:
        start = cur
        cur = start + K
        cnt += 1
    elif arr[cur] == 0:
        cur -= 1
    if cur == start:
        cnt = 0
        break

print(cnt)
    
    
    
    
        
        

    