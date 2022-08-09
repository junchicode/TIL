def BubbleSort(a, N): # 정렬할 list, N 원소 수
    for i in range(N-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

N = int(input())
num = input()
C = [0]*10

for i in num:
    C[int(i)] += 1

res = BubbleSort(C, 10)
ress = res[-1]

for i in range(9, -1, -1):
    if C[i] == ress:
        print(i, ress)

    
        