# 비트마스킹이 이거 같은데... 확인해보자~~
arr = [1,2,3] 
result = []
for i in range(1<<len(arr)): 
  subset = []
  for j in range(len(arr)):
    
    if i & (1<<j): 
      subset.append(arr[j])
      print(bin(i), bin(1<<j))
      
  result.append(subset)
print(result)



