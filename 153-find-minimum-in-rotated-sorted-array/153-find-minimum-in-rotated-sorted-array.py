class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        
        while r-l > 1:
            mid = (r+l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return min(nums[l], nums[r])