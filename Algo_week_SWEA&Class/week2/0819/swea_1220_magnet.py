# 90 turn
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
# input
n = int(input())
m = [list(map(int, input().split())) for _ in range(100)]

#rotate
newm = rotate_90(m)

# new array 
numarr = []
nr = []

for i in m:
    cnt = 0
    for j in i:
        if j != 0:
            nr.append(j)
            cnt += 1
        else: cnt += 1
        if cnt == 100:
            numarr.append(nr)
            nr = []
            cnt = 0 # [[1], [1, 2], [1, 1]] 


# count [1,2]
rescnt = 0            

for i in numarr:
    if len(i) <= 1:
        pass
    else:
        for j in range(1, len(i)):
            if i[j-1] == 1 and i[j] == 2:
                rescnt += 1
                
print(rescnt)
        
            

        
    

