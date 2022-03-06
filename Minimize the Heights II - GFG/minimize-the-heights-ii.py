#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        
        ma = max(arr)
        mi = min(arr)
        if k >= (ma-mi):
            return ma-mi
        arr = sorted(arr)
        u = ma - k
        l = mi + k
        res = ma-mi
        for i in range(n-1):
            mini = min(arr[i+1]-k, l)
            maxi = max(arr[i]+k, u)
            if(mini >=0):
                res = min(res, maxi-mini)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends