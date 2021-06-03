def nCr (n,r):
    res=1
    r=min(r,(n-r))
    for i in range(r):
        res=res*(n-i)/(i+1)
    return res

def findCatalan(n):
    cat=[0]*(n+1)
    if n==0:
        cat[0]=1
        return cat[0]
    if cat[n]==0:
        sum=0
        for i in range(n):
            sum+=findCatalan(i)*findCatalan(n-i-1)
        cat[n]=sum
    return cat[n]

if __name__=="__main__":
    n=int(input())
    cat=nCr(2*n,n)/(n+1)
    print(int(cat))
    print(findCatalan(n))