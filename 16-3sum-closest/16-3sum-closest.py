class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        best = 1001
        for i in range(len(nums) - 2):
            j,k = i+1, len(nums) - 1
            
            while(j < k):
                s = nums[i] + nums[j] + nums[k]
                if abs(best - target) > abs(s - target):
                    best = s
                if s == target:
                    return s
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return best