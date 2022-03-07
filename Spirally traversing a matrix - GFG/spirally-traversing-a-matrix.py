#User function Template for python3
import numpy as np
class Solution:
    def solve(self, arr):
        l = []
        r,c = np.shape(arr)
        if r == 1:
            return list(arr[0,:])
        if c == 1:
            return list(arr[:,0])
        for i in range(c):
            l.append(arr[0,i])
        for i in range(1,r):
            l.append(arr[i,-1])
        for i in range(c-2,-1, -1):
            l.append(arr[-1,i])
        for i in range(r-2,0, -1):
            l.append(arr[i,0])
        if r > 2 and c > 2:
            l.extend(self.solve(arr[1:r-1, 1:c-1]))
        return l
            
        
        
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        return self.solve(np.array(matrix))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends