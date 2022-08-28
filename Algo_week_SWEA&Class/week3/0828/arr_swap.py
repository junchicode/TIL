# 상하 반전
n, m = 2,2

arr = [[1,2],[3,4]]
temp = [[0] * m for _ in range(n)]
 
# 1. 반복문
for i in range(n):
    temp[i] = arr[n-1-i]
 
# 2. 문자열 슬라이싱
'''arr = arr[::-1]

19 20 21 22 23 24 
13 14 15 16 17 18
7 8 9 10 11 12
1 2 3 4 5 6'''

for i in temp:
    print(i)
