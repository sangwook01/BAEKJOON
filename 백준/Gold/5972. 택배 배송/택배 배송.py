'''
1. 시작점이 1로 고정되어 있음 -> 플로워드 워셜이 아닌 다익스트라 알고리즘을 활용해 최단 거리를 갱신해줘야됨
2. 기본적인 다익스트라만 활용해도 좋음
'''
    
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())

start = 1
graph = [[] for i in range(n+1)]
distance = [INF]* (n+1)

for i in range(m):
    a,b,c = map(int, input().split())
    # a에서 b로 가는데 드는 비용 c
    # 양방햐 길
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0
        
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
                
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                          
dijkstra(start)
print(distance[n])   
                        