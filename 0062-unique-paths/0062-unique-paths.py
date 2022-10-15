class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m,n = n,m
            
        if n == 1:
            return 1
        
        if n == 2:
            return m
        
        num,den = 1,1
        for i in range(1, n):
            num *= (m + n - 1 - i)
            den *= i
        
        return num // den
        