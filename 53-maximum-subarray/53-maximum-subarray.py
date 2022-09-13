class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = r = 0
        maxsub = 0
        maxsofar = nums[0]
        
        while r < len(nums):
            maxsub += nums[r]
            maxsofar = max(maxsofar,maxsub)
            r += 1
            if maxsub < 0:
                maxsub = 0
        if maxsofar == 0:
            return max(nums)
        return maxsofar