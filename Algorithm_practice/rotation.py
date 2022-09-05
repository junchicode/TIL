arr = [[0]*3 for _ in range(3)]
start = 1
for i in range(3):
    for j in range(3):
        arr[i][j] = start
        start += 1

def rotate90(arr):
    begin = [[0]*3 for _ in range(3)]
    N = len(arr)
    for i in range(3):
        for j in range(3):
            begin[j][N-1-i] = arr[i][j]
    return begin
print(rotate90(arr))    


