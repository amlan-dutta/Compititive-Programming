n=int(input())
arr=list(map(int,input().split()))
if n>=130: 
    print("Yes")
    exit()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a=arr[i]^arr[j]^arr[k]
            if a in arr:
                print("Yes")
                exit()
print("No")
        