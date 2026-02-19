'''
선수 조건이 있는 문제이기 때문에 위상정렬로 접근해서 풀이를 진행

1. 선수과목을 수강해야지 다음 과목을 들을 수 있음
2. 첫번째에는 총 과목 수 두번째는 선수 조건의 수
3. 다음 줄에는 선수 조건에 대해서 나열 ex. 3 2-> 3번의 선수과목은 2번임
4. 선수과목이 존재할 때 result += 1 but 존재하지 않는다면 result = 1
'''

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

indegree = [0]* (n+1)
graph = [[] for i in range(n+1)]
result = [0] * (n+1)

for _ in range(m):
    # b의 선수 과목은 a => a->b  (즉 a를 들어야 b를 들을 수 있음)
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            # 진입차수가 0인 값에 대해선 선수과목이 존재 X -> 1학기에 바로 가능
            result[i] += 1
            
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1
            # 현재 i에서 선수과목 존재할 시 +1
            result[i] = max(result[i], result[now]+1)
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i], end = ' ')
        
    
topology_sort()
