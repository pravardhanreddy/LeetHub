#User function Template for python3


class Solution:	
	def wineSelling(self, arr, N):
		# code here
		sell = []
		buy = []
		
		for i in range(N-1, -1, -1):
		    if arr[i] < 0:
		        sell.append((i,abs(arr[i])))
		    elif arr[i] > 0:
		        buy.append((i,arr[i]))
        
        ans = 0
        while sell:
            i,s = sell[-1]
            j,b = buy[-1]
            
            if s < b:
                ans += abs(i-j)*s
                sell.pop()
                buy[-1] = (j,b-s)
            elif b < s:
                ans += abs(i-j)*b
                buy.pop()
                sell[-1] = (i,s-b)
            else:
                ans += abs(i-j)*b
                buy.pop()
                sell.pop()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr,N)
        
        print(ans)

# } Driver Code Ends