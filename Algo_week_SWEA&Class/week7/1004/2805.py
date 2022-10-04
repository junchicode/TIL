'''
1
5
14054
44250
02032
51204
52212

#1 23
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    M = N//2
    
    for i in range(N):
        for j in range(abs(M-i), N-abs(M-i)):
            ans += arr[i][j]
            
    