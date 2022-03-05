#User function Template for python3
from collections import Counter
class Solution:
    def sort012(self,arr,n):
        # code here
        c = Counter(arr)
        arr[:c[0]] = [0]*c[0]
        arr[c[0]:c[0]+c[1]] = [1]*c[1]
        arr[c[0]+c[1]:] = [2]*c[2] 
        
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends