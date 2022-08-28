# 상하 반전
n, m = 2,2

arr = [[1,2],[3,4]]
temp = [[0] * m for _ in range(n)]
 
# 1. 반복문
for i in range(n):
    temp[i] = arr[n-1-i]

for i in temp:
    print(i)

# 좌우반전
for i in range(n):
    for j in range(m):
        temp[i][j] = arr[i][m-1-j]
