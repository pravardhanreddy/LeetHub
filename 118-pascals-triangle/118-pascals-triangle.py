class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        if numRows == 1:
            return [[1]]
        result = []
        
        if numRows == 2:
            return [[1],[1,1]]
        prev = [1,1]
        result = [[1],[1,1]]
        curr = []
        
        for i in range(2,numRows):
            curr = [1]
            for j in range(i-1):
                curr.append(prev[j] + prev[j+1])
            curr.append(1)
            prev = curr
            result.append(prev)
        return result