'''
1. 연속된 숫자를 뒤집는 행위를 시도해야됨
2. for문을 통해 전숫자와 다를 경우에만 count
풀이
문자의 젤 앞 뒤가 다르면 (바뀐 횟수 +1)//2
문자의 젤 앞 뒤가 같으면 바뀐 횟수 // 2
but 예외 case
'''
import sys
input = sys.stdin.readline

n = input().strip()

change = 0 
flag = n[0]

for i in list(n):
    
    if i != flag:
        flag = i
        change += 1
        
if n[0] == n[-1]:
    result = change //2 
else:
    result = (change+1)//2
    
print(result)
        