'''
1. 자신의 키의 순서를 알기 위해선 모든 번호와 완전 연결이 되어 있는 상태여야함
2. 최소 경로가 아니라 그냥 경로 연결이 된 경우를 구해야됨
3. 그냥 연결이 된다면 distance에 +1 값을 해준 후 최종적으로 n명의 학생과 같은 수의 distance를 가진 값을 구함
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
# 연결되어 있다면 +1        
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

for i in range(1,n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
                
    if count == n:
        result += 1
        
print(result)

 
