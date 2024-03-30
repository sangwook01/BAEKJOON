number = int(input())
n_dir = int(input())
connect = [sorted(list(map(int,input().split()))) for _ in range(n_dir)]

ans = []
num = []

for i in range(n_dir):
    if connect[i][0] == 1:
        ans.append(connect[i][1])
    
while True:
    if len(ans) == 0:
        break
    
    else:
        num.append(ans.pop(0))
        f_num = num[-1]
        for i in range(n_dir):
            if connect[i][0] == f_num:
                if connect[i][1] not in num:  
                    ans.append(connect[i][1])

            elif connect[i][1] == f_num:
                if connect[i][0] not in num:  
                    ans.append(connect[i][0])

if 1 in num:
    print(len(set(num)) -1)
else:
    print(len(set(num)))
