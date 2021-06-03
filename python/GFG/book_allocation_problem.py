

class Solution:
    def isvalid(self,books,m,value):
        student=1
        pages=0
        for i in books:
            if pages+i<=value:
                pages+=i
            else:
                student+=1
                pages=i
                if student>m:
                    return False
        return True
    def findPages(self,arr, n, m):
        # n: no of book
        # m: no of students
        s=max(arr)
        e=sum(arr)
        while s<=e:
            mid=(s+e)//2
            if (self.isvalid(arr,m,mid)):
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
        #return: the expected answer if possible else return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends