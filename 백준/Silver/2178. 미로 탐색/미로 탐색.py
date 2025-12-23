
'''
1. 미로의 바운더리를 넘으면 안됨
2. 괴물이 있는 부분 (벽) 안됨
3. 처음 방문하는 경우에만 최단 기록으로
'''

from collections import deque

n,m = map(int, input().split())
# 2차원 리스트의 맵 정보 받기

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 상,하,좌,우    
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# BFS 소스 구현
def bfs(x,y):
    
    # 큐 구현을 위해 deque 라이브러리 활용
    queue = deque()
    queue.append((x,y))
    
    # 큐가 빌 때까지 반복 (큐는 먼저 들어온 좌표부터 활용)
    while queue:
        # popleft는 젤 앞 (왼쪽)에 있는 요소부터 제거 후 반환
        x,y = queue.popleft()
        
        # 상,하,좌,우 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 공간을 벗어나면 무시 (n,m)
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # 처음 노드에 방문한 경우 -> 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))