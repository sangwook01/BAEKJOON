import math
n = int(input())
etc = math.floor(math.log(n,2))
if math.log(n,2) == etc:
    print(n)
else:
    print(2*(n-2**(etc)))