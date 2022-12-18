class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        a.sort()
        b.sort()
        
        asum = sum(a)
        bsum = sum(b)
        
        diff = bsum - asum
        
        if diff%2 == 1:
            return -1
        
        for x in a:
            y = (diff + 2*x) // 2
            if binarysearch(b, y):
                return 1
        
        return -1
        
def binarysearch(arr, k):
    l,r = 0, len(arr)-1
    
    while l<=r:
        mid = (l+r) // 2
        if arr[mid] == k:
            return True
        if arr[mid] < k:
            l = mid+1
        else:
            r = mid-1
    return False


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends