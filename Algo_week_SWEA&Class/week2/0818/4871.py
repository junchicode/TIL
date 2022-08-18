def search(s):
    stack.append(s)
    visited[s]=1
    while stack:
        if s==g:
            return 1
        else:
            for i in node[s]:
                if not visited[i]:
                    visited[i]=1
                    stack.append(i)
            s=stack.pop()
    return 0

for t in range(int(input())):
    v,e=map(int,input().split())

    visited=[0]*(v+1)
    node=[[] for _ in range(v+1)]
    stack=[]
    # E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보
    for _ in range(e):
        start,end=map(int,input().split())
        node[start].append(end)
    # E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G
    s,g=map(int,input().split())
    
    print("#{} {}".format(t+1,search(s)))