import sys

sys.stdin = open('input.txt')


def binary_search(nums, target):
    start = 0
    # 인덱스의 끝값은 항상 len(nums)-1
    end = len(nums) - 1
    is_found = False

    # 1. start와 end가 cross되기 전 그리고 target이 발견되기 전까지
    while start <= end and not is_found:
        # 2. mid 포인트를 잡고
        mid = (start + end) // 2
        # 3. 만약에 target이 발견되면 검색 종료
        if nums[mid] == target:
            is_found = True
        # 4. 발견되지 않으면
        else:
            """
            예시.
            17 20 26 31 44 54 55 77 93 -> 31 찾기 / mid - 44
            31 < 44 -> 44 - 1 = 43(end)
            start(0) ~ end(43) 사이에 있을 것

            17 20 26 31 44 54 55 77 93 -> 93 찾기 / mid - 44
            93 > 44 -> 44 + 1 = 45(start)
            start(45) ~ end(len(numbers)-1) 사이에 있을 것
            """
            # 4-1. 만약에 target 값이 더 작으면 end를 내리고
            if target < nums[mid]:
                end = mid - 1
            # 4-2. 크면 start를 올리자
            else:
                start = mid + 1
    return is_found


numbers = list(map(int, input().split()))
print(binary_search(numbers, -9))  # True
print(binary_search(numbers, 20))  # False