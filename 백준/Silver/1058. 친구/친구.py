import sys
input = sys.stdin.readline
count = int(input())
f_lst = []
answer = 0

for _ in range(count):
    f_lst.append(list(map(str,input())))
    
    
for i in range(count):
    lst_Y = list(filter(lambda x: f_lst[i][x] == "Y", range(count)))
    total = lst_Y.copy()
    
    for j in lst_Y:
        lst_Y2 = list(filter(lambda x: f_lst[j][x] == "Y", range(count)))   
        
        total += lst_Y2 
    if len(set(total))-1 > answer:
        answer = len(set(total))-1
    else:
        pass

print(answer)