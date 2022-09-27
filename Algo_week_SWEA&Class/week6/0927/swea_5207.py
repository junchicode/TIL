def bin_s(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if A[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif A[mid] > mid:
        return bin_s(A, target, start, mid-1)
    else:
        return bin_s(A, target, mid+1, end)
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        if bin_s(A, b, 0, N-1):
            ans += 1
    print(ans)
    
                    
    