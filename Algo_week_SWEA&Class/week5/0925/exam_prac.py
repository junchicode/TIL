arr=[1,2,3,4,5]

for i in range(1, len(arr)):
    for j in range(i+1, len(arr)):
        print(arr[:i])
        print(arr[i:j])
        print(arr[j:])