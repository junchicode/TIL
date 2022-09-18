def inorder(node): 
    global cnt
    if node == 0:
        return
    # 전위
    cnt += 1
    inorder(left[node])
    # 중위
    inorder(right[node])
    # 후위

T = int(input())
for tc in range(1, T+1):
    E,N = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left = [0]*(E+2) # 첫번째 자식
    right = [0]*(E+2) # 두번째 자식
    
    for i in range(0,len(arr),2): 
        par, chi = arr[i], arr[i+1] # 부모, 자식
        if left[par]: # 0이 아니고 첫번째에 값이 있으면
            right[par]= chi # 두번째
        else: # 0이면
            left[par]= chi # 첫번째

cnt = 0
inorder(N)
print('#{} {}'.format(tc,cnt))