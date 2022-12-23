#User function Template for python3

class Solution:
    def findOccurrence(self,mat,target):
        
        r = len(mat)
        c = len(mat[0])
        n = len(target)-1
        
        def dfs(i,j,k):
            if i < 0 or i >= r or j < 0 or j >= c or mat[i][j] != target[k]:
                return 0
            
            if k == n:
                return 1
            
            cnt = 0
            
            store = mat[i][j]
            mat[i][j] = '*'
            
            cnt += dfs(i+1,j,k+1)
            cnt += dfs(i-1,j,k+1)
            cnt += dfs(i,j+1,k+1)
            cnt += dfs(i,j-1,k+1)
            
            mat[i][j] = store
            
            return cnt
            
        
        ans = 0
        for i in range(r):
            for j in range(c):
                ans += dfs(i, j, 0)
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        mat=[]
        for _ in range(R):
            mat.append( [x for x in input().strip().split()] )
        target=input()
        obj = Solution()
        print(obj.findOccurrence(mat,target))
# } Driver Code Ends