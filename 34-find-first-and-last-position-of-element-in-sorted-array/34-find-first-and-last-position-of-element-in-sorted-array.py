class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        start, end = 0, len(nums)-1
        startSet, endSet = False, False
        startSet = nums[start] == target
        endSet = nums[end] == target
        if startSet and endSet:
            return [start, end]
        
        l,r = 0, len(nums)
        if not startSet:
            while l<r:
                m = (r-l) // 2
                if nums[l+m] == target:
                    if nums[l+m-1] < target:
                        start = l+m
                        startSet = True
                        break
                    else:
                        r = l+m
                elif nums[l+m] < target:
                    l += m+1
                else:
                    r = l+m
        l,r = 0, len(nums)
        if not endSet:
            while l<r:
                m = (r-l) // 2
                if nums[l+m] == target:
                    if nums[l+m+1] > target:
                        end = l+m
                        endSet = True
                        break
                    else:
                        l += m
                elif nums[l+m] < target:
                    l += m+1
                else:
                    r = l+m
        return [start,end] if startSet and endSet else [-1,-1]