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

## append랑 pop을 쓰지 않고 하는 또다른 방법

num = int(input())

q = []


for i in range(num):
    act = input().split()
    if act[0] == 'push':
        qq = [int(act[1])]
        qq[:-1] = q
        q = qq
        
        temp = act[1]

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
            print(q[0])
            q = q[1:]

