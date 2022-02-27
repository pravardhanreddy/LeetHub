#User function Template for python3
import numpy as np

class Solution:
    def smallestSubstring(self, S):
        # Code here
        pos = [-np.inf] * 3
        ans = np.inf
        
        for i,c in enumerate(S):
            pos[int(c)] = i
            ans = min(ans, 1 + i - min(pos))
        return -1 if np.isinf(ans) else ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends