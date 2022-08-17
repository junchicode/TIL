arr = list(map(int, input().split()))

# 찾고자 하는 데이터
key = -9

for i in range(len(arr)):
    if key == arr[i]:
        print(i, ' 에 위치하고 있음')
        break
else:
    print('못찾음')