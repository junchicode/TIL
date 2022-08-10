arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(1<<n):                 # 1<<n : 부분지합개수
    for j in range(n):                # 원소의 수만큼 비트를 비교
        if i & (i<<j):                # i의 j번 비트가 1인 경우
            print(arr[j], end = ", ") # j번 원소 출력
    print() 
print()