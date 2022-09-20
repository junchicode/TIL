E = int(input())
arr = list(map(int, input().split()))
V = E + 1
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    