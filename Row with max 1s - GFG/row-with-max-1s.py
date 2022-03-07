#User function Template for python3
from collections import Counter
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		m = 0
		mi = -1
		
		for i in range(n):
            c = Counter(arr[i])[1]
            if c > m:
                m = c
                mi = i
        return mi
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends