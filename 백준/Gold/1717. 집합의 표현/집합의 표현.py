'''
합집합을 의미하는 것은 0 -> union_parent
같은 집합에 포함되는지 확인하는 것 1 -> find_parent => 같은 집합에 속하느냐? == a,b가 같은 부모 아래 있는가?
N의 값이 1,000,000까지로 범위가 매우 넓음.... 
일반적인 서로소 집합 자료 구조를 활용하기엔 무리가 있음.. => 런타임 에러 발생
1. 이때 바꿀 수 있는 것 (재귀적 함수 호출을 while문으로 변경...)
2. 재귀 호출의 횟수 늘리기 (이건 코딩테스트에 있어서 별로 좋지 않은 구조라 생각)
3. path halving이라는 것이 존재! 해당 개념을 활용해보자!

'''

import sys
input = sys.stdin.readline
'''
해당 함수를 재귀가 아닌 while문으로 변경 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 일반적인 while문
def find_parent(parent, x):
    root = x
    while parent[root] != root:
        root = parent[root]

    # 경로 압축
    while parent[x] != x:
        next_x = parent[x]
        parent[x] = root
        x = next_x

    return root
'''
# pass halving을 적용
def find_parent(parent,x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
n,m = map(int, input().split())

parent = [0]*(n+1)
for i in range(0,n+1):
    parent[i] = i

# 0,1에 따라서 각 함수를 다르게 수행해야됨
for i in range(m):
    oper, a, b = map(int,input().split())
    if oper == 0:
        union_parent(parent, a, b)
        
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent, b) :
            print("YES")
        else:
            print("NO")

