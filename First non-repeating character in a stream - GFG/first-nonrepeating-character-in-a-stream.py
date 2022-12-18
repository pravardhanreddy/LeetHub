#User function Template for python3
from collections import deque
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		seen = set()
		repeated = set()
		q = deque()
		
		ans = []
		
		for a in A:
		    if a not in seen:
		        seen.add(a)
		        q.append(a)
		        ans.append(q[0])
		    else:
		        repeated.add(a)
		        while q and q[0] in repeated:
		            q.popleft()
		        if q:
		            ans.append(q[0])
		        else:
		            ans.append('#')
	    return ''.join(ans)
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends