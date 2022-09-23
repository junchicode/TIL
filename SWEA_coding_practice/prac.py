list = [1,2,3,4,5]

for i in range(5):
    for j in range(1, 5):
        if len(list[:i]) == 0:
            pass
        else:
            print(list[:i])
            
        
        