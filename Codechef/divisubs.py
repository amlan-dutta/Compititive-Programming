
import sys
def find(arr,n):
    s=[None]*(n+1)
    s[0]=0
    su=0
    for i in range(1,n+1):
        su=(su+arr[i-1])%n
        if s[su] is not None:
            print(i-s[su])
            #print(s,i)
            for j in range(s[su],i):
                sys.stdout.write(str(j+1)+" ")
            sys.stdout.write("\n")
            return 0
        else:
            s[su]=i
    print(-1)

t=int(input())
for _ in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    find(arr,n)
    