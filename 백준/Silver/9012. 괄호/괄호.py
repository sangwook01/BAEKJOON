number = int(input())
vps = [(input()) for i in range(number)]
for i in range(number):
    a = 0
    result = []
    for j in vps[i]:
        if j == '(':
            result.append(j) 
        else:
            if result == []:     
                a += 1
            else:
                result.pop()
    if a == 0 and len(result) == 0:
        print("YES")
    else:
        print("NO")