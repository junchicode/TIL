import math
n = int(input())
idx = math.floor(n/2)
nlist = list(map(int, input().split()))

nlist.sort()
print(nlist[idx])
