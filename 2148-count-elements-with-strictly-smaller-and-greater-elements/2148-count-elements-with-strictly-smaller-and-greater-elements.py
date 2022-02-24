class Solution:
    def countElements(self, nums: List[int]) -> int:
        mi = min(nums)
        ma = max(nums)
        
        return len(nums) - nums.count(mi) - nums.count(ma) if (mi != ma) else 0 