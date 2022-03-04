class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d and target == n*2:
                return [i, d[n]]
            else:
                d[n] = i
                if target - n in d:
                    if d[n] != d[target-n]:
                        return [d[n], d[target - n]]
                
            