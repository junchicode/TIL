from operator import truediv
import turtle


def binarysearch(a, N, key): #검색대상 배열, 초기크기, 찾고자하는 대상
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] ==key: # 검색성공
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle +1
    return False # 검색실패
             