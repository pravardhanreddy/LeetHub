class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range(n//2):
            for i in range(n - 2*l - 1):
                matrix[l+i][n-l-1], matrix[n-l-1][n-l-i-1], matrix[n-l-i-1][l], matrix[l][l+i] = matrix[l][l+i], matrix[l+i][n-l-1], matrix[n-l-1][n-l-i-1], matrix[n-l-i-1][l]
