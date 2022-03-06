#User function Template for python3

class Solution:
    
    def solve(self, arr, start, end):
        if start == end:
            return arr[start]
        if start == end-1:
            return arr[start] if arr[start] < arr[end] else arr[end]
        n = (end - start)//2
        if arr[start + n] > arr[end]:
            return self.solve(arr, start + n, end)
        else:
            return self.solve(arr, start, start+n)
    
    
    def findMin(self, arr, n):
        #complete the function here
        return self.solve(arr, 0, n-1)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends