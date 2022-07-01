from collections import deque

class MyQ:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        # remove all elements from the end that are less than x
        while len(self.q):
            if self.q[-1] < x:
                self.q.pop()
            else:
                break
        self.q.append(x)
        
    def pop(self, x):
        if len(self.q) == 0:
            return None
        if self.q[0] == x:
            return self.q.popleft()
        return self.q[0]
        

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def maxSlidingWindow(self, A, B):
        if B > len(A):
            return max(A)
        
        q = MyQ()
        for i in range(B-1):
            q.push(A[i])
        
        ans = []
        for i in range(B-1, len(A)):
            q.push(A[i])
            ans.append(q.pop(A[i-B+1]))
            
        return ans
