'''
1. 길이가 짧은 순서대로
2. 길이가 같다면 사전 순서대로
3. 단, set으로 중복제거하기
<생각>
문자열을 정렬하는 과정에서는 tuple 형태를 활용하면 보다 편하게 구현할 수 있음
(a,b)-> 왼쪽부터 차례대로 조건에 맞게 바꿈
<과정>
3번 과정 먼저 수행
1,2 순서로 sort에 대해 lambda 함수 구현하기

'''
import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(input().strip())

# 중복제거    
lst = list(set(lst))

lst.sort(key = lambda x: (len(x),x))    
 
for c in lst:
    print(c)
