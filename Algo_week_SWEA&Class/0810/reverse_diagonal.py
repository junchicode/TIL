N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# case 1
sum = 0
for i in range(N):
    sum += arr[i][N-1-i]