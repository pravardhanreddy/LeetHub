import collections
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[-1] * len(text2) for _ in text1]

        def solution(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if matrix[i][j] != -1:
                return matrix[i][j]
            
            if text1[i] == text2[j]:
                matrix[i][j] = 1 + solution(i+1, j+1)
            else:            
                matrix[i][j] = max(solution(i+1,j), solution(i,j+1))
            return matrix[i][j]
                

        return solution(0, 0)