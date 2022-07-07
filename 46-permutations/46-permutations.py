from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = deque(nums)
        if len(nums) == 1:
            return [nums.copy()]
        for _ in range(len(nums)):
            n = nums.popleft()
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)
        
        return result
            
        
        
        