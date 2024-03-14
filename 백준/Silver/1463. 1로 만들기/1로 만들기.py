count = 0
lst = [0,1,1] 
num = int(input())
if num <= 3:
        pass
else:
    for i in range(3,num):
        if (i+1) % 6 == 0:
            lst.append(min((lst[((i+1)//3)-1]),(lst[((i+1)//2)-1]),(lst[i-1]))+1)
        
        elif (i+1) % 2 == 0:
            lst.append(min((lst[((i+1)//2)-1]),(lst[i-1]))+1)
        
        elif (i+1) % 3 == 0:
            lst.append(min((lst[((i+1)//3)-1]),(lst[i-1]))+1)
        else:
            lst.append(lst[i-1]+1)

print(lst[num-1]) 