#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		m = arr[0]
		rmf, rmb = 1,1
		
		for i in range(n):
    	    rmf *= arr[i]
    	    rmb *= arr[n-i-1]
    	    m = max([m, rmf, rmb])
    	    if rmf == 0:
    	        rmf = 1
    	    if rmb == 0:
    	        rmb = 1
		return m
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends