'''
One of the important properties of gray code is that every two adjacent numbers have exactly one different 
digit in their binary representation.
In this problem, we will give you n non-negative integers in a sequence A[1..n] (0<=A[i]<2^64), such that 
every two adjacent integers have exactly one different digit in their binary representation, similar to 
the Gray code.
Your task is to check whether there exist 4 numbers A[i1], A[i2], A[i3], A[i4] (1<= i1< i2 < i3 < i4 <= n) 
out of the given n numbers such that A[i1] xor A[i2] xor A[i3] xor A[i4] =0. Here xor means bitwise xor.

'''
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