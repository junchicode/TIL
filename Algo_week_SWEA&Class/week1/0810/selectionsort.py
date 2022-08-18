def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                min = j
        a[i], a[minIdx] = a[minIdx], a[i]