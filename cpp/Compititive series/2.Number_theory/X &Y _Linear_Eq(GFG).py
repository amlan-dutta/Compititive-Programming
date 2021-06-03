'''
Given A, B and N. Find x and y that satisfies equation Ax + By = N. If there's no solution print -1 in 
place of both x and y.

Note: There are Multiple solutions possible. Find the solution where x is minimum. x and y should both be 
      non-negative.
'''

class Solution:
    def findXandY(self, A , B , N):
    # Liner diaphantine equaltion for Ax+By=N, here unsolvable case means when any of x, y is less than 0
        if N%B==0:
            return [0,N//B]
        else:
            x=1
            while(N-x*A)>0:
                if (N-x*A)%B==0:
                    break
                else:
                    x+=1
            if (N-x*A)>=0:
                return [x,(N-x*A)//B]
            else:
                return [-1,-1]
            #-1,-1 is not a solution, just an indication for no possible solution for both x > 0 , y > 0

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,N=map(int,input().split())
        
        ob = Solution()
        ptr = ob.findXandY(A,B,N)
        print(*ptr)
