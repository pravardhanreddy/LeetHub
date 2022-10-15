class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows < 2:
            return s
        
        mat = ['']*numRows
        
        j, k = 0, 0
        step = 1
        while k < len(s):
            mat[j] += s[k]
            
            k += 1
            
            if j == numRows-1:
                step = -1
            elif j == 0:
                step = 1
            j += step
        
        return ''.join(mat)