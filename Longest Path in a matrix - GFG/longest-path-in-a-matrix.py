#User function Template for python3

class Solution:
	def longestIncreasingPath(self, matrix):
		#Code here
		
		r = len(matrix)
		p = len(matrix[0])
		
		dp = [[0]*p for _ in range(r)]
		m = 0
		
		def paths(i,j, prev):
		    if i<0 or i >= r or j < 0 or j >= p or (prev is not None and matrix[i][j] <= prev):
		        return 0
		    if dp[i][j] != 0:
		        return dp[i][j]
		    c = 0
		    c = max(c, paths(i+1,j,matrix[i][j]))
		    c = max(c, paths(i-1,j,matrix[i][j]))
		    c = max(c, paths(i,j+1,matrix[i][j]))
		    c = max(c, paths(i,j-1,matrix[i][j]))
		    dp[i][j] = c+1
		    return c+1
		    
		    
		    
		for i in range(r):
		    for j in range(p):
		        m = max(m, paths(i,j, None))
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.longestIncreasingPath(matrix)
		print(ans)

# } Driver Code Ends