import sys
input = sys.stdin.readline
number = int(input())
lst = [int(input()) for i in range(number)]
last_num = lst[-1]
max_num = max(lst)
result = []
for i in reversed(lst):
    if i >= last_num:
        result.append(i)
        last_num = i
    elif i == max_num:
        result.append(i)
        break
print(len(set(result)))