class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        start = [0]*len(nums)
        start[0] = nums[0]
        start[1] = max(nums[0], nums[1])
        
        
        for i in range(2, len(nums)):
            start[i] = max(start[i-2]+nums[i], start[i-1])
        
        return start[-1]