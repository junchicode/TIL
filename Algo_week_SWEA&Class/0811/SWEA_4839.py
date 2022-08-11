def BinarySrch(a, N, key):
    start = 0
    end = N-1
    cnt = 0
    while start <= end:
        middle = (start + end)//2
        cnt += 1
        if a[middle] == key:
            return cnt
        elif a[middle] > key:
            end = middle
            
        else:
            start = middle
            
            
    return False

T = int(input())
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())
    pa = pa-1
    pb = pb-1
    book = [i for i in range(p)]
    caseB = BinarySrch(book, p, pb) #B
    caseA = BinarySrch(book, p, pa) #A
   
    if caseA < caseB:
        res = "A"
    elif caseA > caseB:
        result = "B"
    else:
        result = 0  
    print(f'#{tc} {result}')
