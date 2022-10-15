class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows < 2:
            return s
        
        mat = [['']*numRows]
        
        i, j, k = 0, 0, 0
        while k < len(s):
            mat[i][j] = s[k]
            
            k += 1
            
            if i % (numRows-1) or j == numRows-1:
                mat.append(['']*numRows)
                i += 1
                j -= 1
            else:
                j += 1
        
        ans = ''
        for j in range(numRows):
            for i in range(len(mat)):
                ans += mat[i][j]
        return ans