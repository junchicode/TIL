def Counting_Sort(A, B, k):
    # A [] -- 입력 배열 (1 to k)
    # B [] -- 정렬된 배열
    # C [] -- 카운트 배열

    C = [0] * (k+1) # 빈 count 배열

    for i in range(0, len(A)):
        C[A[i]] += 1
    
    for i in range(1, len(C)): # 누적 과정
        C[i] += C[i-1]
    
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
