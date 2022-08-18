def BubbleSort(a, N): # 정렬할 list, N 원소 수
    for i in range(N-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

N, M = map(int, input().split())
arr = list(map(int, input().split()))
resl = []
for i in range(N-M-1):
    res = 0
    for j in range(M):
        res += arr[i+j]
    resl.append(res)
        
sortres = BubbleSort(resl, len(resl))

print(sortres[-1] - sortres[0])
        
        
    
    
    