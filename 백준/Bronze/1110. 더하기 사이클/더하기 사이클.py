'''
str => len
한자리 수에 대해서 앞에 0을 붙여주는 작업을 수행
'''
import sys
input = sys.stdin.readline

n = input().strip()

if len(n) == 1:
    n = '0' + n
    
cycle = 0
start = n

while True:
    
    result = str(int(n[0]) + int(n[1]))
    if len(result) == 1:
        result = '0' + result
    n = n[1] + result[-1] 
    cycle += 1
    
    if n == start:
        break

print(cycle)

