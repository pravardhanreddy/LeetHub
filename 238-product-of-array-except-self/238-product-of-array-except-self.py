from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        pre,suf = 1,1
        for i in range(n):
            res[i] *= pre
            pre *= nums[i]
            res[n-i-1] *= suf
            suf *= nums[n-i-1]
        return res
        