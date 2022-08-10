def binary_search(arr, low, high, key):
    if low > high:
        return -1
    
    else:
        middle = (low + high) // 2
        if arr[middle] == key:
            return middle
        elif key < arr[middle]:
            return binary_search(arr,low, middle-1, key)
        elif key > arr[middle]:
            return binary_search(arr, middle+1, high, key)