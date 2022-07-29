T = int(input())
for tc in range(T):
    n,m = map(int, input().split())
    area = [list(map(int, input().split())) for  _ in range(n)]
    
    move = n - m + 1
    areal = []
    idxl = []
    for i in range(move):
        for j in range(move):
            sum = 0
            for ic in range(m):
                for jc in range(m):
                    areal.append(area[i+ic][j+jc])
                    print([i, ic],[j, jc],[i+ic],[j+jc], "하나씩할경우 : ", [i, j, ic, jc])
    print(areal)
                    
                    
                
                    
                    