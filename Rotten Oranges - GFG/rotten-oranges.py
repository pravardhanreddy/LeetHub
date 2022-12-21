import collections
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		ans = 0
		
		rotten = {}
		fresh = set()
		
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 1:
		            fresh.add((i,j))
		        elif grid[i][j] == 2:
		            rotten[(i,j)] = 0
        max_d = len(grid)*len(grid[0])
        
        changed = True
        while fresh and changed:
            # print(fresh)
            # print(rotten)
            still_fresh = set()
            changed = False
            for i,j in fresh:
                dist = max_d # init to high
                if (i+1,j) in rotten:
                    dist = min(dist, rotten[(i+1,j)]+1)
                if (i-1,j) in rotten:
                    dist = min(dist, rotten[(i-1,j)]+1)
		        if (i,j+1) in rotten:
                    dist = min(dist, rotten[(i,j+1)]+1)
                if (i,j-1) in rotten:
                    dist = min(dist, rotten[(i,j-1)]+1)
                
                if dist < max_d:
                    # print(i,j,dist)
                    rotten[(i,j)] = dist
                    changed = True
                else:
                    still_fresh.add((i,j))
                    
            fresh = still_fresh
        
        if not changed:
            return -1
        
        for i,j in rotten:
            dist = rotten[(i,j)] # init to high
            if (i+1,j) in rotten:
                dist = min(dist, rotten[(i+1,j)]+1)
            if (i-1,j) in rotten:
                dist = min(dist, rotten[(i-1,j)]+1)
	        if (i,j+1) in rotten:
                dist = min(dist, rotten[(i,j+1)]+1)
            if (i,j-1) in rotten:
                dist = min(dist, rotten[(i,j-1)]+1)
            ans = max(ans, dist)
        return ans
        


#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends