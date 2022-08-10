# 몇 번 행의 값이 가장 커?
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0 # 최대 행의 합
for i in range(N):
    rowsum = 0 # 행의 합
    for j in range(N): # i행의 j열에 접근
        rowsum += arr[i][j]
    if maxV < rowsum:
        maxV = rowsum

print(maxV)