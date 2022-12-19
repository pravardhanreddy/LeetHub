#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        
        # we take 1 move to a floor.
        # If egg breaks, then we can check dp[m – 1][x – 1] floors.
        # If egg doesn’t break, then we can check dp[m – 1][x] floors.
        dp = [[0]*(n+1) for _ in range(k+1)]
        
        m = 0
        while (dp[m][n] < k):
            m+=1
            for x in range(1,n+1):
                dp[m][x] = 1 + dp[m - 1][x - 1] + dp[m - 1][x]
            
        
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends