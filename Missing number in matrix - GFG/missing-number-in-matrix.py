#User function Template for python3
import numpy as np
class Solution:
	def MissingNo(self, matrix):
		# Code here
		zero = None
		
        n = len(matrix)

        
        mat = np.array(matrix)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero = (i,j)
                    break
            if zero is not None:
                break
        
        tr = 0 if zero[0] != 0 else 1
        
        s = sum(matrix[tr])
        
        zs = sum(matrix[zero[0]])
        
        matrix[zero[0]][zero[1]] = s - zs
        mat[zero[0], zero[1]] = s - zs
        
        # verify conditions
        
        rsum = mat.sum(axis = 0)
        csum = mat.sum(axis = 1)
        
        if any(rsum != s) or any(csum != s):
            return -1
        
        if np.diag(mat).sum() != s or np.diag(mat[:,::-1]).sum() != s:
            return -1
        
        return (s - zs) if (s - zs) > 0 else -1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.MissingNo(matrix)
		print(ans)

# } Driver Code Ends