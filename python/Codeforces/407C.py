mod=1000000007
n,m=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(m):
    l,r,k=map(int,input().split())
    C,rng=1,(r-l+1)
    for j in range(rng):
        a[l+j-1]=int((a[l+j-1]+C+mod)%mod)
        C=(C*(k+j+1)/(j+1))%mod

print(*a)

    