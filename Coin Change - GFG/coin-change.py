#User function Template for python3

class Solution:
    def count(self, coins, N, s):
        # code here 
        dp = [0]*(s+1)
        dp[0] = 1
        for i in range(N):
            for j in range(coins[i], s+1):
                dp[j] += dp[j-coins[i]]
        # print(dp)
        return dp[s]
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends