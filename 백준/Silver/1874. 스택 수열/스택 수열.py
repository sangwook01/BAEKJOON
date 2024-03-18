import sys
input = sys.stdin.readline
count = int(input())
stack = [int(input()) for i in range(count)]
answer = ''
past = 0
lst = []
Flag = True

for i in range(count):
    number = stack[i]
    if number > past:
        answer += '+\n'*(number- past)
        answer += '-\n'
        for j in range(number - past):
            past += 1
            lst.append(past)
        lst.pop()
         
    else:
        if number == lst[-1]:
            answer += '-\n'
            lst.pop()
        else:
            Flag = False
if Flag:
    print(answer)
else:
    print("NO")