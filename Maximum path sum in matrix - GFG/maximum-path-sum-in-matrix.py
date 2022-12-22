#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        grid = [[0]*(N+2) for _ in range(N-1)]
        grid = grid + [[0] + Matrix[-1] + [0]]
        # print(len(grid), len(grid[0]), len(grid[1]))
        for i in range(N-2, -1, -1):
            for j in range(1,N+1):
                # print(i,j)
                grid[i][j] = Matrix[i][j-1] + max(grid[i+1][j], grid[i+1][j-1], grid[i+1][j+1]) 
        return max(grid[0])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends