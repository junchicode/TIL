def bubble(array):
    length = len(array)
    for i in range(length-1, -1, -1):
        for j in range(0, i-1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

arr = [9,2,3,2,1,7,8,4,10,20]

print(bubble(arr))                