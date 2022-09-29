'''1   2   3   -1

-2  -3  4    5

6   -2  -4   -2

-1   3   2   3
----

1  3  6  5

-1 0  10 15
9  11   14  10'''
n, m = map(int, input().split())
brd = [list(map(int, input().split())) for _ in range(m)]

for i in range(1, n):
    brd[0][i] = brd[0][i] + brd[0][i-1]
    
for i in range(1, n):
    for j in range(n):
            
        try: brd[i][j] += max(brd[i-1][j], brd[i][j+1])
    
        except: brd[i][j] += brd[i-1][j]
    
print(brd)

