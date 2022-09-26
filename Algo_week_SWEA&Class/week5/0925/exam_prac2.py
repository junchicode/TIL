nums = list(map(int, input().split()))
cnt = 0
for i in range(min(nums),0,-1):
    for j in range(len(nums)):
        if nums[j]%i == 0:
            cnt += 1
            if cnt == len(nums):
                print(i)
                exit()
        else:
            cnt = 0
            break
    
    
        
        
        