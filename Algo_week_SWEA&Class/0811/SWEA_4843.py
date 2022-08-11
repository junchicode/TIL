def bubble_sort(numbers):
    for i in range(len(numbers)-1,0,-1):
        for j in range(0,i):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    srtarr = bubble_sort(arr)
    res = []
    while True:
        res.append(srtarr[len(srtarr)-1])
        del srtarr[len(srtarr)-1]
        if len(srtarr) == 0:
            break
        res.append(srtarr[0])
        del srtarr[0]
        if len(srtarr) == 0:
            break
    res = " ".join(map(str,res[:10]))
    print(f"#{tc} {res}")
    