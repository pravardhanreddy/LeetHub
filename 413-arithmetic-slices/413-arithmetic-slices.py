import numpy as np
class Solution:
    
    def solve(self, arr):
        if len(arr) < 3:
            return 0
        diff = arr[1] - arr[0]
        l = 0
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] == diff:
                l += 1
            elif l == 0:
                return l*(l+1)//2 + self.solve(arr[1:])
            else:
                return l*(l+1)//2 + self.solve(arr[i-1:])
        return l*(l+1)//2
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return self.solve(np.array(nums))
        