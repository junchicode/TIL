n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n-m+1):
    for j in range(n-m+1):
        sum = 0
        for ic in range(m):
            for jc in range(m):
                sum += arr[i+ic][j+jc]
                
        # m사각형 한번 다 돌고 (ex: 2*2=4 크기의 사각형)
        if sum > res:
            res = sum
            
print(res)
                

                