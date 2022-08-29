score_list = [1,1,2,2,5,7]

for i in range(1,5):
    for j in range(i+1, 6):
        
        low = score_list[:i]
        middle = score_list[i:j]
        high = score_list[j:]
        print([low, middle, high])
    