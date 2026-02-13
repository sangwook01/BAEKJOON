'''
크루스칼 알고리즘을 활용하는 대표적인 문제
1.집과 집을 연결하는데 최소 비용을 활용하고 싶음
2. 서로소의 자료구조를 활용
3. find_parent, union_parent 함수 구현하고 parent 테이블 정의 및 자기자신으로 초기화
4. result 값으로 나온 것은 최소 비용으로 구축된 길을 만드는데 사용되는 비용 
5. 지금 마을을 두개로 분리해야되기 때문에 크루스칼을 활용하되 마지막에 가장 큰 값을 빼주어야됨
'''
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())

parent = [0] * (n+1)

edges = []
result = 0

for i in range(1,n+1):
    parent[i] = i
    
for i in range(m):
    a,b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort() # 오름차순으로 정렬해서 비용이 최소인 것부터 선택
max_cost = 0 # 최소 신장 트리를 만족하는 것 중에 가장 큰 수
             # 마을을 2개로 분리해야되기 때문에 마지막 하나는 끊어줘야됨
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost
        
print(result - max_cost)
    
    