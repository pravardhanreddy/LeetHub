import numpy as np

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = np.sort(heights)
        
        output = [index for index,a in enumerate(heights) if a != expected[index]]
        return len(output)