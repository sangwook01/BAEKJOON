'''
기본적인 플로이드 워셜 
but 조건에 노선이 하나가 아닐 수 있음 -> 중복된 간선이 존재할 수 있음
'''

INF = int(1e9)
# 노드와 간선의 수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가능 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용 c
    a,b,c = map(int, input().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 플로이드 워셜 알고리즘 수행

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
# 수행된 결과물 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, 0출력
        if graph[a][b] == INF:
            graph[a][b] = 0
        print(graph[a][b], end = ' ')
    print()