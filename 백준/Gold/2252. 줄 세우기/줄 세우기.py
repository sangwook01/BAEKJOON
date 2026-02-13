'''
1. 학생들의 키를 비교하고 그에 따른 순서를 나타내는 것 
2. 방향성을 거스르지 않고 순서대로 나열하는 문제로 판단
3. 위상정렬 알고리즘 활용
'''

from collections import deque

# 노드의 개수와 간선의 개수 입력받기
v,e = map(int, input().split())
# 모든 노드에 대해서 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력 받기
for _ in range(e):
    a,b = map(int, input().split())
    # a -> b
    graph[a].append(b)
    # 진입차수 1증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 리스트에 담기
    q = deque() # 큐 기능을 위한 deque 라이브러리 활용
    
    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 추출
        now = q.popleft()
        # 해당 원소와 연결된 노드에서 진입차수 1 빼기
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                    
    # 위상 정렬을 수행한 결과 출력
    for i in result:    
        print(i, end = ' ')

topology_sort()