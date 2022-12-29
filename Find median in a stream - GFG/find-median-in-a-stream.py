#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''

class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)
            else:
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return -self.max_heap[0]
        
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        if not self.min_heap or x > self.min_heap[0]:
            heapq.heappush(self.min_heap, x)
        else:
            heapq.heappush(self.max_heap, -x)
        self.balanceHeaps()
        
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends