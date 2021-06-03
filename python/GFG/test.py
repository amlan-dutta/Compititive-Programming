#User function Template for python3
class Solution:

	def _sum(self,arr, n):
   		# code here
   		if n==0:
   		    return 0
   		else:
   		    return (arr[n-1]+self._sum(arr,n-1))


#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        ob = Solution()
        ans = ob._sum(arr, n)
        print(ans)
        tc=tc-1
# } Driver Code Ends