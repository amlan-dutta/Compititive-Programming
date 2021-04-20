'''
You are given N number of books. Every ith book has Ai number of 
pages. 
You have to allocate books to M number of students. There can be 
many ways or permutations to do so. In each permutation, one of 
the M students will be allocated the maximum number of pages. Out 
of all these permutations, the task is to find that particular 
permutation in which the maximum number of pages allocated to a 
student is minimum of those in all the other permutations and 
print this minimum value. 

Each book will be allocated to exactly one student. Each student 
has to be allocated at least one book.

Constraints:
        1 <= N <= 10^5
        1 <= A [i] <= 10^6
        1 <= M <= 10^5

Example 1:
    Input:
        N = 4
        A[] = {12,34,67,90}
        M = 2
    Output:
        113
    Explanation: 
        Allocation can be done in following ways:
        {12} and {34, 67, 90} Maximum Pages = 191
        {12, 34} and {67, 90} Maximum Pages = 157
        {12, 34, 67} and {90}  Maximum Pages =113
        Therefore, the minimum of these cases is 
        113, which is selected as the output.
'''

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
        #maximum page read by any student can be atleast max_page
        #and atmost sum of all pages
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



if __name__=='__main__':
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    m=int(input())
    ob=Solution()
    print(ob.findPages(arr,n,m))
