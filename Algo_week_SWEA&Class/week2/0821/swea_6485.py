T = int(input())
for tc in range(1, T+1):
    N = int(input())
    busdict = {}

    for i in range(1, 5001):
        busdict[i] = 0
    
    for i in range(N):
        s, e = map(int,input().split())
        for j in range(s, e+1):
            busdict[j] += 1
    
    P = int(input())
    res = []
    
    for i in range(P):
        res.append(busdict[int(input())])
        
    print(f"#{tc}", *res)
        