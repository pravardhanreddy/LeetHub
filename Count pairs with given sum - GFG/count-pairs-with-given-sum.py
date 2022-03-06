#User function Template for python3
from collections import Counter
class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        
        c = Counter(arr)
        s = 0
        
        for a in c:
            if k-a in c:
                s += (c[a]*c[k-a])/2 if a!= k-a else (c[a]*(c[a]-1))//2
        return int(s)
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends