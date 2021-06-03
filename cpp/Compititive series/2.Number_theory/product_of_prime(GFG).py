
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
        
    def primeProduct(self, L, R):
        #array of prime numbes from 2 to root(R)
        root=int(math.sqrt(R))+1
        primes=self.sieveOfEratosthenes(root)  
        #pick each numbers from list and mark every multiple of this from L to R as a non-prime     
        isPrime=[True]*(R-L+1)
        for i in (primes):
            base=(L//i)*i
            if base<L:
                base+=i
            for j in range(base, R+1, i):
                isPrime[j-L]=False
            if base==i:
                isPrime[base-L]=True
        mul=1
        for i in range(R-L+1):
            if isPrime[i]:
                mul*=(i+L)%1000000007     
        return mul%1000000007


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.primeProduct(L, R))