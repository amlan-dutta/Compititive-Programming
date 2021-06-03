class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        col,row=C+1,len(A)+1
        #mat=[[0 for i in range(col)] for j in range(row)]
        mat=[[0]*col]*row 
        print()
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    continue
                elif B[i-1]<=j: #if possible to include
                    include_value = A[i-1]+mat[i-1][j-B[i-1]]
                    exclude_value = mat[i-1][j]
                    mat[i][j]= max(include_value,exclude_value)
                else:
                    mat[i][j]=mat[i-1][j]
        return mat[0]
        
if __name__=="__main__":
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=int(input())
    o=Solution()
    k=o.solve(a,b,c)
    print(k)