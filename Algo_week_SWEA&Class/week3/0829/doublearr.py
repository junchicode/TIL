score_list = [1,1,2,2,5,7]

for i in range(1,5):
    for j in range(i+1, 6):
        
        low = sum(score_list[:i])
        middle = sum(score_list[i:j])
        high = sum(score_list[j:])
        print([low, middle, high])
    