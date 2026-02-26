'''
문자열 정렬기의 사전식 규칙
1. 접두사의 경우 X가 Y의 접두사 인 경우 -> X,Y 순서 => 파이썬에서 자동으로 sort 가능
2. 접두사가 아닌 경우
2-a. 달라지는 부분이 붙임표일 경우 -> 붙임표가 있는 것이 후순위
2-b. 달라지는 부분이 붙임표가 아닐 경우 
2-b-1. 달라지는 부분이 같은 단어 -> 대소문자 순서
2-b-2. 달라지는 부분이 다른 단어 -> 알파벳 순서 (대소문자 신경 X)

파이썬에 존재하는 append함수 제대로 활용할 줄 알아야됨
tuple 형태로 고정하게 되면 왼쪽 부터 순차적으로 검사하기 때문에 조건을 잘 설정해야됨
'''

import sys
input = sys.stdin.readline


def custom(word):
    key = []
    
    for c in word:
        # 붙임표일 경우
        if c == '-':
            key.append((1,)) # "-" 접두사를 가장 뒤에 보낸다.
        # 붙임표가 아닐경우
        else:
            # c.lower() 다른 단어의 경우 알파벳 순서, c 같은 단어의 경우 대소문자
            # c.lower()가 먼저인 경우는 대소문자를 먼저 비교하면 a, B의 경우 B가 우선 순위가 되어버림
            key.append((0,c.lower(), c))
    return key

n = int(input())
lst = []

for _ in range(n):
    in_lst = []
    m = int(input())
    for _ in range(m):
        in_lst.append(input().strip())
    lst.append(in_lst)

for e in lst:
    e.sort(key = custom)
    for result in e:
        print(result)