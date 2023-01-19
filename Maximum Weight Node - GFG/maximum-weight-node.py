#User function Template for python3
from collections import defaultdict
class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        d = defaultdict(int)
        
        for i,j in enumerate(Edge):
            d[j] += i
        
        m = 0
        ind = N-1
        for j in range(N-1, -1, -1):
            if d[j] > m:
                m = d[j]
                ind = j
        return ind

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends