'''
항상 숫자는 짝수 -> 인덱스 값을 기준으로 len(list)/2 전까지 더하고 나머지 더해서 합이 같은지 확인
'''
import sys
input = sys.stdin.readline

n = input().strip()

num_lst = list(map(int, n))
         
result_left = 0
result_right = 0
index = 0   

for i,j in enumerate(num_lst):
    if i < len(num_lst)//2:
         result_left += j
         
    else:
         result_right += j

if result_left == result_right:
    print("LUCKY")
else:
    print("READY")