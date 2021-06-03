'''

'''

import math
class Solution:
    def sieveOfEratosthenes(self,N): 
        N+=1
        p=[True]*N
        p[1]=False
        # every even number except 2 is not prime
        for i in range(0,N,2):
    	    p[i]=False
        p[2]=True
        # multiple of every prime in range from 3 to root(N) is not prime
        r=int(math.sqrt(N))+1
        for i in range(3,r,2):
    	    if p[i]==True:
    	        for l in range(i*i,N,i):
    	            p[l]=False
        arr=[]
        for i in range(N):
    	    if p[i]:
    	        arr.append(i)
        return arr


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()