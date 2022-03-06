#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n==1:
	        return 0
	    i = 0
	    jumps = 1
	    while(i<n):
            if arr[i] + i >= n-1:
                return jumps
            if arr[i] == 0:
                return -1
            m,mi = -1,0
            for j in range(1, arr[i]+1):
                if arr[i+j] - arr[i] + j > m:
                    m = arr[i+j] - arr[i] + j
                    mi = j
            i += mi
            jumps+=1
        return jumps

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends