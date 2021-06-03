'''
Q:  You are given a multiset of N integers. Please find such a nonempty subset of it that the sum of the 
    subset's elements is divisible by N. Otherwise, state that this subset doesn't exist.

    The first line consists of a single integer N - the size of the multiset.The second line contains N 
    single space separated integers - the multiset's elements.

    If the required subset exists, output two lines. Output the size of the subset on the first line and 
    output the list of indices of the multiset's element that form the required subset. Any number can 
    be taken in the subset not more than once. If there are several such subsets, you can output any.
'''

import sys
def find(arr,n):
    s=[None]*n
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

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    find(arr,n)
    