#User function Template for python3
def binarySearch(nums, target):
    l, r = 0, len(nums)
    while l < r :
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else: 
            r = m
    return l

class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,a,b,M,N):
        #code here
        a.sort()
        ans = 0
        i = 0
        while a[i] == 1:
            i += 1
        
        ones = i
        
        while a[i] == 2:
            i += 1
        
        twos = i - ones
        
        while a[i] == 3:
            i += 1
        
        threes = i - ones - twos
        
        for y in b:
            if y > 4:
                ind = binarySearch(a,y)
                ans += ind - ones
            else:
                if y == 1:
                    ans += M - ones
                elif y == 2 or y == 4:
                    ans += threes
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        M,N=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        ob=Solution();
        print(ob.countPairs(a,b,M,N))
        #code here
# } Driver Code Ends