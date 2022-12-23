from typing import List


class Solution:
    def findMaxValue(self, n : int, mat : List[List[int]]) -> int:
        # code here
        r = len(mat)
        c = len(mat[0])
        
        mx = mat[-1][-1]
        for i in range(r-1, -1, -1):
            mx = max(mx, mat[i][-1])
            mat[i][-1] = mx
        mx = mat[-1][-1]
        for j in range(c-1, -1, -1):
            mx = max(mx, mat[-1][j])
            mat[-1][j] = mx
        
        ans = -10000000
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                ans = max(ans, mat[i+1][j+1] - mat[i][j])
                mat[i][j] = max([mat[i][j], mat[i+1][j], mat[i][j+1]])
        # for row in mat:
        #     print(row)
        return ans
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        mat=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.findMaxValue(n, mat)
        
        print(res)
        

# } Driver Code Ends