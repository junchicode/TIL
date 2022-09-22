# 그래프 탐색 (DFS)

# 1) 스택을 이용한 DFS 구현
def dfs_stack(graph, start):
    visited = []
    stack = []
    
    # 시작 노드 스택에 담기   
    stack.append(start)
    
    # 스택에 방문하지 않은 인접 정점들을 담은 후 하나씩 빼오면서 탐색
    while stack:
        now = stack.pop()
        if now not in visited: 
            visited.append(now)
            stack.extend(graph[now])

    return ' '.join(visited)


# 2) 재귀함수를 이용한 DFS 구현
visited = []
def dfs_recursive(graph, start):
    # 이미 방문한 노드라면 탐색 종료
    if start in visited:
        return
    
    # 방문 표시
    visited.append(start)
    print(start, end=' ')

    # 인접 정점들에 대해 재귀 호출
    for now in graph[start]:
        dfs_recursive(graph, now)


graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

print(dfs_stack(graph, 'A'))  
print(dfs_recursive(graph, 'A'))