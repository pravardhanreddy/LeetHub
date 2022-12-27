#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if A[0][0] != 1:
            return -1
        
        q = deque()
        visited = set()
        steps = 0
        q.append((0,0))
        
        while q:
            n = len(q)
            for _ in range(n):
                x,y = q.popleft()
                if x < 0 or x>=N or y < 0 or y >= M or ((x,y) in visited) or A[x][y] == 0  :
                    continue
                if x == X and y == Y:
                    return steps
                    
                q.append((x+1,y))
                q.append((x-1,y))
                q.append((x,y+1))
                q.append((x,y-1))
                
                visited.add((x,y))
            steps += 1
        return -1
                
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends