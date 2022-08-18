
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sum = 0
for i in range(N):
    for j in range(N):
        sum += arr[i][j]

print(sum)
        