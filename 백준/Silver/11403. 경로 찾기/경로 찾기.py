'''
플로워드 워셜로 푸는 문제
but 기존과는 다르게 행렬 자체가 주어짐
점화식을 세우는 것을 생각하자!
길이 생길려면 ij도 존재하지만 (i+k) + (k+j) 또한 길이 생김
'''

INF = 1e9
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1

for a in range(n):
    for b in range(n):
        print(graph[a][b], end = ' ')
    print()
            
      