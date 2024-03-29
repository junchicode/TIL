from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
	# 큐 구현을 위해 deque 라이브러리 사용
	queue = deque([start])  
	# 현재 노드 방문처리
	visited[start] = True
	
	# 큐가 빌 때까지 반복
	while queue:
		# 큐에서 원소를 뽑아 출력
		v = queue.popleft()
		print(v, end=' ')
		# 아직 방문하지 않은 인접 원소들을 큐에 삽입
		for i in graph[v]: # v = 인덱스
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9
# False = 한 번도 인접하지 않는 것으로 초기화

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)