'''
maxV -< arr[0]
for i : 1 -> N - 1
    if max[:] > maxV
        maxV -< arr[:]
'''

N = int(input())
arr = list(map(int, input().split()))
maxV = arr[0] # 첫 원소를 최댓값으로 가정
for i in range(1, N): # 나머지 모든 원소에 대해
    if arr[i] > maxV:
        maxV = arr[i]

print(maxV)
