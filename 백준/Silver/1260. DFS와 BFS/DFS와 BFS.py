from collections import deque

N,M,V = map(int,input().split())

# 2차원 인접 리스트
graph = [[] for _ in range(N+1)]
for _ in range(M):       
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 정점이 여러개인 경우 정점 번호가 작은 것을 우선으로 처리해야됨
for i in range(1, N+1):
    graph[i].sort()
    
    
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
            
# BFS 메소드 정의
def bfs(graph, start, visited):
    # queue 구현을 위핸 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # queue가 빌 때까지 반복
    while queue:
        # queue에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
bfs_visited =[False] * (N+1)
dfs_visited =[False] * (N+1)
 
dfs(graph,V,dfs_visited)
print()
bfs(graph,V,bfs_visited)
