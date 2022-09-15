for tc in range(int(input())):
                                                
    N, M, L = map(int, input().split())         # 노드 N개, 리프노드 M개, 출력노드 L번
    tree = [0 for _ in range(N+1)]              # 루트노드 번호가 1이니 +1
   
    for _ in range(M):                          # 리프노드번호와 값 입력받고 트리에 대입
        idx, value = map(int, input().split())  # 4,1 -> 5,2 -> 3,3
        tree[idx] = value
                                                #[0, 0, 0, 3, 1, 2]
    for i in range(N, 0, -1): 
        # 마지막 노드부터 역순으로 부모노드 값 대입
        if i // 2 > 0:                          # i를 2로 나눈 몫이 0보다 크다면                       
            tree[i//2] += tree[i]               # 값을 더해줌
            
    print(f'#{tc+1} {tree[L]}')