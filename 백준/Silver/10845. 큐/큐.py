import sys
input = sys.stdin.readline
num = int(input())

q = []


for i in range(num):
    act = input().split()
    if act[0] == 'push':
        q.append(int(act[1]))
        
    elif act[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    elif act[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    
    elif act[0] == 'size':
        print(len(q))
        
    elif act[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif act[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))

