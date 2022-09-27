
def qs(arr, start, end):
    if start >= end: # 원소가 1인 경우 종료
        return
    pivot = start    # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right: 
        # 피벗보다 큰 데이터 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:            # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행
    qs(arr, start, right-1)
    qs(arr, right+1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qs(arr, 0, len(arr)-1)
    print(f'#{tc} {arr[int(N/2)]}')

