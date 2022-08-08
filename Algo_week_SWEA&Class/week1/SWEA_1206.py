N = int(input())
bdlist = list(map(int, input().split()))
res = 0
for i in range(2, N-2):
    tmp = bdlist[i]
    tmpn = 257
    for j in range(i-2, i+3):
        if j == i:
            pass
        else:
            if tmp - bdlist[j] < tmpn: 
                tmpn = tmp - bdlist[j]
    
    if tmpn > 0:
        res += tmpn
        
print(res)