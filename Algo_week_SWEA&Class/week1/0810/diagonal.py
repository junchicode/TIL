N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# case 1
sum = 0
for i in range(N):
    for j in range(N):
        if i == j:
            sum += arr[i][j]
# case 2      
sum = 0
for i in range(N):
    sum += arr[i][i]