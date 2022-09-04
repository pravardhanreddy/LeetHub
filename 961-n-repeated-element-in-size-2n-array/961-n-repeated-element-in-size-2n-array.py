class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set(nums)
        return (sum(nums) - sum(s)) // ((len(nums) // 2)-1)
        