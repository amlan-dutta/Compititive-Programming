#Given an integer, the task is to find factorial of the number.(A large number)

import sys
size=5000

def fac(n):
    res=[None]*size
    res[0]=1
    res_size=1
    if n!=0 and n!=1:
        x=2
        while x<=n:
            res_size=mul(x,res,res_size)
            x+=1
    i=res_size-1
    while i>=0:
        sys.stdout.write(str(res[i]))
        i-=1
    sys.stdout.write("\n")

def mul(a,arr,s):
    carry=0
    i=0
    while i<s:
        prod=arr[i]*a+carry
        arr[i]=prod%10
        carry=prod//10
        i+=1
    while carry:
        arr[s]=carry%10
        carry=carry//10
        s+=1
    return s
    
if __name__=='__main__':
    n=int(input())
    sys.stdout.write(str(n)+" factorial is : ")
    fac(n)