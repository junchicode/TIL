arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
lenarr = len(arr)

for i in range(1, lenarr-1):
    for j in range(i+1, lenarr):
        st = arr[:i]
        mid = arr[i:j]
        end = arr[j::]

        print(st, mid, end)