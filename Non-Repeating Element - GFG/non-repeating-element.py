#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        c = Counter(arr)
        for a in arr:
            if c[a] == 1:
                return a
        return 0
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends