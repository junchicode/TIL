def bubble(a):
    for i in range(len(a)-1, -1, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

list =  [3,12,23,4,5]

print(bubble(list))