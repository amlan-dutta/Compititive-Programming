import math
t=int(input())
for _ in range(t):  
    p=int(input())
    if p==2 or p==3:
        print("YES")
        continue
    if p%2==0:
        print("NO")
        continue
    flag=1
    root=math.ceil(math.sqrt(p))
    for i in range(3,root+1):
        if p%i==0:
            flag=0
            print("NO")
            break
    if flag==1:
        print("YES")