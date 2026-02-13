'''
1. 출발 위치, 도착 위치가 존재 -> 시작 위치는 무조건 0
2. 지름길의 도착위치는 고속도로의 길이보다 길어선 안됨
3. 지름길이 존재한다면 지름길 중에 가장 짧은 길이를 선택해야되지만 그게 아닐 시엔 그냥 일반적인 길이를 선택해야됨
4. 지름길의 길이를 노드로 잡으면 안되는 이유 -> 지름길이 항상 좋은 선택을 보이지 않을 수도 있기 때문에!!
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,d = map(int, input().split())

start = 0
# 지름길이 존재할 수도 안할 수도 있기 때문에 
graph = [[] for i in range(d+1)]

# 기본적인 도로의 길이는 1이기 때문에
for i in range(d):
    graph[i].append((i+1,1))
    
    
distance = [INF] * (d+1)

# 간선 정보 입력 받기
for i in range(n):
    a,b,c = map(int, input().split())
    # a에서 b로 가는 지름길의 길이는 c
    # 전체 길이보다 지름길의 도착 위치가 길면 안됨
    if b<=d:
        graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q) # 
        
        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q,(new_cost,next_node))

dijkstra(start)

print(distance[d])
            