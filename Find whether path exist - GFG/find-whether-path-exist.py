import collections
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		#Code here
		q = collections.deque()
		start = None
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 1:
		            start = (i,j)
		
        q.append(start)
        
        while q:
            i,j = q.popleft()
            if not (0<=i<len(grid) and 0<=j<len(grid[0])) or grid[i][j] == 0:
                continue
            
            if grid[i][j] == 2:
                return 1
            
            grid[i][j] = 0
            q.append((i+1,j))
            q.append((i-1,j))
            q.append((i,j+1))
            q.append((i,j-1))
        
        return 0
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends