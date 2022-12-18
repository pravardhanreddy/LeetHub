#User function Template for python3
import functools
 
# A comparison function which
# is used by sort() in
# printLargest()
def myCompare(x, y):
    xy = x+y
    yx = y+x
 
    return 1 if xy > yx else -1
 
# The main function that prints
# the arrangement with the
# largest value. The function
# accepts a vector of strings

    
    
class Solution:

    def printLargest(self, arr):
     
        # Sort the numbers using
        # library sort function. The
        # function uses our comparison
        # function myCompare() to
        # compare two strings. See
     
        arr.sort(key=functools.cmp_to_key(myCompare), reverse=True)
     
        return "".join(map(str, arr))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends