n,k=map(int,input().split())
arr=list(map(int,input().split()))
dis=[arr[0]]
poss=[0]
for i in range(1,n):
    if i-poss[0]>k:
        dis.pop(0)
        poss.pop(0)
    temp=dis[0]*arr[i]
    while dis[-1]>temp and len(dis)!=0:
        dis.pop(-1)
        poss.pop(-1)
    dis.append(temp)
    poss.append(i)
print(dis[-1]% 1000000007)